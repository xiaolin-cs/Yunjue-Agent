# Copyright (c) 2026 Yunjue Tech
# SPDX-License-Identifier: Apache-2.0
import json
import logging
from pathlib import Path
from typing import Any, List, Tuple

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, ToolMessage

from src.schema.types import LLMType, ResponseAnalysis, ToolExecutionRecord
from src.services.llms.llm import create_llm, get_max_tokens
from src.prompts.loader import prompt_loader
from src.tools.dynamic_tool_loader import count_text_tokens, get_dynamic_tools

logger = logging.getLogger(__name__)


BASIC_TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools" / "basic"


# The three tools below form the ReAct agent's "basic tool" set and are always
# available regardless of whether any dynamic tool directory is configured:
#   * image_text_query   – in-process langchain ``@tool`` wrapper around the
#                           vision LLM (needs direct access to ``create_llm``),
#                           defined in ``src/tools/image_text_query.py``.
#   * fetch_web_text     – subprocess-isolated crawl4ai page fetcher, lives in
#                           ``src/tools/basic/fetch_web_text.py``.
#   * web_search         – subprocess-isolated Tavily web search, lives in
#                           ``src/tools/basic/web_search.py``.
# The split between ``get_preset_tools`` and ``get_basic_tools`` is purely an
# execution-model detail; conceptually they are one set.
def get_preset_tools() -> List[Any]:
    """In-process basic tools shipped with the repo.

    Currently the only member is ``image_text_query``, which uses the shared
    ``create_llm(LLMType.VISION)`` client and therefore cannot run inside the
    isolated dynamic-tool subprocess.
    """
    from src.tools.image_text_query import image_text_query

    return [image_text_query]


def get_basic_tools(user_query: str = "") -> List[Any]:
    """Subprocess-isolated basic tools bundled under ``src/tools/basic``.

    These follow the standard ``__TOOL_META__`` / ``InputModel`` / ``run``
    convention and are loaded via the same path as user-provided dynamic tools,
    but they ship with the repo so they are always available to the agent.
    Currently the bundle contains ``fetch_web_text`` and ``web_search``.
    """
    BASIC_TOOLS_DIR.mkdir(parents=True, exist_ok=True)
    return get_dynamic_tools(str(BASIC_TOOLS_DIR), user_query)


async def load_available_tools(
    dynamic_tools_private_dir: str,
    dynamic_tools_public_dir: str,
    user_query: str,
) -> List[Any]:
    """Assemble the full tool list handed to the ReAct agent.

    Layers (in return-list order, lowest → highest priority on name collision):

        1. ``get_preset_tools()`` – in-process basic tools (``image_text_query``).
        2. ``get_basic_tools()``  – bundled subprocess-isolated basic tools
           (``fetch_web_text``, ``web_search``).
        3. Public dynamic tools   – loaded from ``dynamic_tools_public_dir``.
        4. Private dynamic tools  – loaded from ``dynamic_tools_private_dir``
           and override any earlier tool sharing the same name.

    The preset (in-process) tools are appended without dedup so that no dynamic
    tool can accidentally shadow them.
    """
    preset_tools = get_preset_tools()
    basic_tools = get_basic_tools(user_query)
    dynamic_private_tools = get_dynamic_tools(dynamic_tools_private_dir, user_query)
    dynamic_public_tools = get_dynamic_tools(dynamic_tools_public_dir, user_query)

    merged: dict[str, Any] = {tool.name: tool for tool in basic_tools}
    for tool in dynamic_public_tools:
        merged[tool.name] = tool
    for tool in dynamic_private_tools:
        merged[tool.name] = tool

    return preset_tools + list(merged.values())


async def analyze_response(pending_response: str) -> Tuple[bool, str]:
    """Judge whether the given worker response concludes the task successfully.

    Uses the ``analyze_response.md`` prompt with ``LLMType.BASIC`` to produce a
    ``ResponseAnalysis`` verdict. Returns ``(is_finish, reason)``:
      * ``is_finish=True`` → the response is conclusive and the task is done (FINISH).
      * ``is_finish=False`` → the response is inadequate and the worker should retry (RETRY).
    Any analyzer failure is treated conservatively as FINISH=False so the caller can
    decide whether to retry based on its own retry budget.
    """
    if not pending_response or not pending_response.strip():
        return False, "Response is empty."

    prompt_content = prompt_loader.get_prompt(
        "analyze_response.md",
        pending_response=pending_response,
    )
    llm = create_llm(LLMType.BASIC).with_structured_output(
        ResponseAnalysis,
        method="json_mode",
    )

    try:
        analysis_result = await llm.ainvoke([HumanMessage(content=prompt_content)])
    except Exception as exc:
        logger.error(f"analyze_response LLM invocation failed: {exc}")
        return False, f"Analyzer error: {exc}"

    status = (getattr(analysis_result, "status", "RETRY") or "RETRY").upper()
    reason = getattr(analysis_result, "reason", "") or ""
    logger.info(f"analyze_response verdict={status} reason={reason}")
    return status == "FINISH", reason


async def summarize_context(
    user_query: str,
    history_tool_executions: List[ToolExecutionRecord],
    context_summary: str,
    is_recur_limit_exceeded: bool = False,
):
    """Summarize the context of the current task and the history tool executions."""
    tool_execution_histories = (
        transform_tool_executions_to_str(history_tool_executions) if history_tool_executions else ""
    )
    tmp_context_summary = context_summary
    for tool_execution_history in tool_execution_histories:
        prompt_content = prompt_loader.get_prompt(
            "context_summarizer.md",
            **{
                "user_query": user_query,
                "tool_execution_history": tool_execution_history,
                "context_summary": tmp_context_summary,
                "enable_tool_usage_feedback": is_recur_limit_exceeded,
            },
        )

        llm = create_llm(LLMType.BASIC)
        messages = [HumanMessage(content=prompt_content)]

        try:
            response = await llm.ainvoke(messages)
        except Exception as e:
            logger.error(f"LLM ainvoke failed: {e}")
            raise

        response = getattr(response, "content", response)
        if isinstance(response, list):
            summary = "".join(
                part if isinstance(part, str) else json.dumps(part, ensure_ascii=False)
                for part in response
            )
        else:
            summary = str(response)
        logger.info(f"Summarized context from {len(tool_execution_history)} to {len(summary)}")
        tmp_context_summary = summary
    return tmp_context_summary


def transform_tool_executions_to_str(
    tool_executions: List[Any], current_context_summary: str = ""
) -> List[str]:
    """Transform tool executions to a list of text chunks bounded by token limit."""

    if current_context_summary:
        tool_history_parts = [current_context_summary]
    else:
        tool_history_parts = []
    for i, exec_record in enumerate(tool_executions, 1):
        tool_name = getattr(exec_record, "tool_name", "unknown")
        arguments = getattr(exec_record, "arguments", {})
        result = getattr(exec_record, "result", None)
        error = getattr(exec_record, "error", None)

        tool_call_str = f"### Tool Call {i}: {tool_name}\n\n"
        tool_call_str += (
            f"**Arguments:**\n```json\n{json.dumps(arguments, indent=2, ensure_ascii=False)}\n```\n\n"
        )
        if error:
            tool_call_str += f"**Error:** {error}\n\n"
        elif result:
            tool_call_str += f"**Result:**\n```\n{str(result)}\n```\n\n"
        else:
            tool_call_str += "**Status:** ⏳ Pending/Unknown\n\n"

        tool_history_parts.append(tool_call_str)

    llm_token_limit = get_max_tokens(LLMType.BASIC)

    tool_execution_histories: List[str] = []
    current_parts: List[str] = []
    current_tokens = 0

    for part in tool_history_parts:
        part_tokens = count_text_tokens(part)
        if current_parts and (current_tokens + part_tokens > llm_token_limit):
            tool_execution_histories.append("\n".join(current_parts))
            current_parts = [part]
            current_tokens = part_tokens
        else:
            current_parts.append(part)
            current_tokens += part_tokens

    if current_parts:
        tool_execution_histories.append("\n".join(current_parts))

    return tool_execution_histories


def extract_tool_calls_from_messages(all_messages: List[BaseMessage]) -> List[ToolExecutionRecord]:
    """Extract tool call / result pairs from a message list."""
    tool_call_map: dict[str, dict[str, Any]] = {}
    for message in all_messages:
        if isinstance(message, AIMessage) and getattr(message, "tool_calls", None):
            for tool_call in message.tool_calls:
                tool_call_id = (
                    tool_call.get("id") if isinstance(tool_call, dict) else getattr(tool_call, "id", None)
                )
                tool_name = (
                    tool_call.get("name") if isinstance(tool_call, dict) else getattr(tool_call, "name", None)
                )
                args = (
                    tool_call.get("args") if isinstance(tool_call, dict) else getattr(tool_call, "args", {})
                )
                if tool_call_id:
                    tool_call_map[tool_call_id] = {
                        "tool_name": tool_name or "unknown",
                        "arguments": args,
                        "caller_message_id": message.id,
                    }

    new_tool_executions: List[ToolExecutionRecord] = []
    for message in all_messages:
        if isinstance(message, ToolMessage):
            tool_call_id = message.tool_call_id
            tool_result = message.content
            tool_message_id = message.id
            error_msg = None
            if hasattr(message, "status") and message.status == "error":
                error_msg = str(tool_result) if tool_result else "Tool execution failed"

            if tool_call_id and tool_call_id in tool_call_map:
                info = tool_call_map[tool_call_id]
                new_tool_executions.append(
                    ToolExecutionRecord(
                        caller_message_id=info["caller_message_id"],
                        tool_message_id=tool_message_id,
                        tool_name=info["tool_name"],
                        tool_call_id=tool_call_id,
                        arguments=info["arguments"],
                        result=tool_result if not error_msg else None,
                        error=error_msg,
                    )
                )
            elif tool_call_id:
                logger.warning(f"Tool call without matching AIMessage: {tool_call_id}")

    for tool_call_id, info in tool_call_map.items():
        if not any(record.tool_call_id == tool_call_id for record in new_tool_executions):
            new_tool_executions.append(
                ToolExecutionRecord(
                    caller_message_id=info["caller_message_id"],
                    tool_name=info["tool_name"],
                    tool_call_id=tool_call_id,
                    arguments=info["arguments"],
                    result=None,
                )
            )

    return new_tool_executions


def format_conversation(all_messages: List[BaseMessage], max_len: int = 500) -> str:
    """Pretty-print a React agent conversation for logging."""
    lines = []
    for i, m in enumerate(all_messages):
        prefix = f"[{i:02d}]"
        if isinstance(m, HumanMessage):
            lines.append(f"{prefix} User: {str(m.content)}")
        elif isinstance(m, AIMessage):
            lines.append(f"{prefix} Agent: {str(m.content)}")
            if getattr(m, "tool_calls", None):
                for tc in m.tool_calls:
                    name = getattr(tc, "name", None) or tc.get("name")
                    args = getattr(tc, "args", None) or tc.get("args", {})
                    lines.append(f"    └ tool_call -> {name} args={args}")
        elif isinstance(m, ToolMessage):
            lines.append(f"{prefix} Tool: {str(m.content)}")
        else:
            lines.append(f"{prefix} {type(m).__name__}: {m}")
    return "\n".join(lines)
