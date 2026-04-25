# Copyright (c) 2026 Yunjue Tech
# SPDX-License-Identifier: Apache-2.0
import logging
from typing import Annotated, Any, AsyncIterator, List, Literal, Optional, TypedDict

from typing_extensions import NotRequired

from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    RemoveMessage,
    SystemMessage,
    ToolMessage,
)
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langgraph.types import Command

from src.agents.memory import MemoryAnalyzer
from src.schema.types import LLMType
from src.utils.context_trimmer import ContextTrimmer
from src.utils.utils import analyze_response
from src.services.llms.llm import get_max_tokens
from src.prompts.loader import prompt_loader

logger = logging.getLogger(__name__)

AgentPrevNode = Literal["__start__", "context_summary", "rollback", "check_response"]


class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]
    # Counts how many times we've transitioned into the "tools" node.
    tool_steps: int
    # Counts how many times we've retried (rollback).
    retry_count: int
    tool_call_cnt: int
    # Set by the node that hands off to `agent`: START initial input, `context_summary`, or `rollback`.
    agent_prev_node: NotRequired[AgentPrevNode]


class ReActAgent:
    def __init__(
        self,
        llm,
        tools,
        max_steps: Optional[int] = None,
        max_retries: Optional[int] = 10,
        user_query: str = None,
        context_summary: str = None,
        query_id: str = None,
        exp_name: str = None,
    ):
        """
        ReAct-style agent built with LangGraph, with integrated memory analysis.

        Args:
            llm: Base chat model instance.
            tools: Tool list passed to the underlying ToolNode + model tool binding.
            max_steps: Optional maximum number of tool-execution iterations.
            max_retries: Optional maximum number of retry attempts (rollback). Defaults to 10.
        """
        self.max_steps = max_steps
        self.max_retries = max_retries

        self.tools = tools
        self._llm_base = llm
        self._llm_with_tools = llm.bind_tools(self.tools)
        self.tool_node = ToolNode(self.tools)

        self.user_query = user_query
        llm_token_limit = get_max_tokens(LLMType.BASIC)
        self.context_trimmer = ContextTrimmer(llm_token_limit, user_query=user_query)
        self.context_summary = context_summary
        self.query_id = query_id
        self.memory_analyzer = MemoryAnalyzer(self._llm_base, query_id, exp_name=exp_name)

        workflow = StateGraph(AgentState)
        workflow.add_node("agent", self.call_model)
        workflow.add_node("tools", self.call_tools)
        workflow.add_node("context_summary", self.context_summary_internal)
        workflow.add_node("rollback", self.rollback)
        workflow.add_node("check_response", self.check_response)
        workflow.add_edge(START, "agent")
        workflow.add_conditional_edges("agent", self.should_continue)
        workflow.add_edge("tools", "context_summary")
        workflow.add_edge("context_summary", "agent")
        workflow.add_edge("rollback", "agent")

        self.graph = workflow.compile()

    @staticmethod
    def is_response_empty(response) -> bool:
        """Check if response content is empty."""
        if hasattr(response, "tool_calls") and response.tool_calls:
            return False

        content = getattr(response, "content", response)
        if isinstance(content, list):
            content_text = "".join(part if isinstance(part, str) else str(part) for part in content)
        else:
            content_text = str(content) if content is not None else ""

        return not content_text.strip()

    def context_summary_internal(self, state: AgentState):
        new_state = context_summary(state, self.context_trimmer)
        if isinstance(new_state, dict):
            return {**new_state, "agent_prev_node": "context_summary"}
        return new_state

    @staticmethod
    def _human_message_text(msg: HumanMessage) -> str:
        content = msg.content
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            return "".join(part if isinstance(part, str) else str(part) for part in content)
        return str(content) if content is not None else ""

    @staticmethod
    def _is_snapshot_message(msg: BaseMessage) -> bool:
        return getattr(msg, "name", None) == "Progress"

    def _update_task_status(self, msg: HumanMessage) -> None:
        text = ReActAgent._human_message_text(msg)
        if "# Current Instruction" in text:
            tid = self.memory_analyzer.parse_instruction_task_id_from_snapshot_text(text)
            if tid:
                self.memory_analyzer.mark_task_done_in_tasks_json(tid)

    def call_model(self, state: AgentState):
        tool_steps = state.get("tool_steps", 0)
        retry_count = state.get("retry_count", 0)
        agent_prev_node = state.get("agent_prev_node", "__start__")
        logger.debug("call_model: agent_prev_node=%s", agent_prev_node)
        messages = list(state["messages"])

        self.memory_analyzer.analyze_and_persist_call_input(messages, tool_steps, retry_count)
        self.memory_analyzer.write_snapshot_md(task_objective=self.user_query or "")
        if self.max_steps is not None and tool_steps >= self.max_steps:
            return {
                "messages": ["Recur limit exceeded"],
                "tool_steps": tool_steps,
                "retry_count": retry_count,
            }

        system_prompt = prompt_loader.get_prompt(
            "worker.md",
            **{
                "user_query": self.user_query,
                "failure_report": None,
                "context_summary": self.context_summary,
            },
        )
        messages.insert(0, SystemMessage(content=system_prompt))
        snapshot_text = self.memory_analyzer.read_snapshot_md()
        if snapshot_text.strip():
            snapshot_message = HumanMessage(content=snapshot_text, name="Progress")
            self._update_task_status(snapshot_message)
            messages.append(snapshot_message)

        response = self._llm_with_tools.invoke(messages)
        return {"messages": [response], "tool_steps": tool_steps, "retry_count": retry_count}

    def call_tools(self, state: AgentState):
        last_message = state["messages"][-1]
        current = state.get("tool_steps", 0)
        tool_call_cnt = state.get("tool_call_cnt", 0)
        next_steps = current + 1
        if isinstance(last_message, AIMessage) and getattr(last_message, "tool_calls", None):
            tool_call_cnt += len(last_message.tool_calls)

        result = self.tool_node.invoke(state)
        if isinstance(result, dict):
            result["tool_steps"] = next_steps
            result["tool_call_cnt"] = tool_call_cnt
        return result

    def rollback(self, state: AgentState):
        """Remove the second-to-last AIMessage and all subsequent messages after an empty response."""
        messages = state["messages"]
        tool_steps = state.get("tool_steps", 0)
        retry_count = state.get("retry_count", 0) + 1

        ai_message_indices = [i for i, msg in enumerate(messages) if isinstance(msg, AIMessage)]

        if len(ai_message_indices) < 2:
            logger.warning(
                f"Less than 2 AIMessages found ({len(ai_message_indices)}), removing last message only"
            )
            if messages:
                return {
                    "messages": [RemoveMessage(id=messages[-1].id)],
                    "tool_steps": tool_steps,
                    "retry_count": retry_count,
                    "agent_prev_node": "rollback",
                }
            return {"retry_count": retry_count, "agent_prev_node": "rollback"}

        second_to_last_ai_idx = ai_message_indices[-2]
        messages_to_remove = messages[second_to_last_ai_idx:]

        has_tool_messages = any(isinstance(msg, ToolMessage) for msg in messages_to_remove)
        if has_tool_messages and tool_steps > 0:
            tool_steps -= 1

        remove_messages = [RemoveMessage(id=msg.id) for msg in messages_to_remove]

        logger.info(
            f"Rollback: removing {len(remove_messages)} messages, "
            f"tool_steps: {tool_steps}, retry_count: {retry_count}"
        )

        return {
            "messages": remove_messages,
            "tool_steps": tool_steps,
            "retry_count": retry_count,
            "agent_prev_node": "rollback",
        }

    def should_continue(
        self, state: AgentState
    ) -> Literal["tools", "rollback", "check_response", "__end__"]:
        last_message = state["messages"][-1]
        tool_steps = state.get("tool_steps", 0)
        retry_count = state.get("retry_count", 0)

        if self.max_retries is not None and retry_count >= self.max_retries:
            logger.warning(
                f"Retry limit exceeded ({retry_count} >= {self.max_retries}), ending execution"
            )
            return END

        if self.is_response_empty(last_message):
            logger.warning("Empty response detected, routing to rollback node")
            return "rollback"

        tool_calls = getattr(last_message, "tool_calls", None)
        if tool_calls:
            if self.max_steps is not None and tool_steps >= self.max_steps:
                logger.warning(
                    f"Tool step limit exceeded ({tool_steps} >= {self.max_steps}), routing to end node"
                )
                return END
            return "tools"

        logger.info(
            "No tool calls on final AIMessage; routing to check_response for analyzer verdict"
        )
        return "check_response"

    @staticmethod
    def _last_ai_text(messages: List[BaseMessage]) -> str:
        """Extract plain text from the most recent AIMessage in ``messages``."""
        for msg in reversed(messages):
            if isinstance(msg, AIMessage):
                content = getattr(msg, "content", "")
                if isinstance(content, str):
                    return content
                if isinstance(content, list):
                    return "".join(
                        part if isinstance(part, str) else str(part) for part in content
                    )
                return str(content) if content is not None else ""
        return ""

    async def check_response(
        self, state: AgentState
    ) -> Command[Literal["agent", "__end__"]]:
        """Judge whether the latest AI response concludes the task.

        * FINISH verdict → route to END.
        * RETRY verdict → increment ``retry_count`` (shared budget with ``rollback``),
          append a ``HumanMessage`` carrying the analyzer's ``reason`` so the next
          ``call_model`` invocation is aware of why the previous answer was rejected,
          then route back to the ``agent`` node.
        * If ``retry_count`` would exceed ``max_retries`` after incrementing, route to END.
        """
        retry_count = state.get("retry_count", 0)
        messages = state.get("messages", [])
        pending_response = self._last_ai_text(messages)

        try:
            is_finish, reason = await analyze_response(pending_response)
        except Exception as exc:
            logger.error(f"check_response analyzer failed, ending: {exc}")
            return Command(goto=END)

        if is_finish:
            logger.info(f"check_response verdict=FINISH, ending. reason={reason}")
            return Command(goto=END)

        new_retry_count = retry_count + 1
        if self.max_retries is not None and new_retry_count >= self.max_retries:
            logger.warning(
                f"check_response wanted retry but budget exhausted "
                f"({new_retry_count} >= {self.max_retries}); ending. reason={reason}"
            )
            return Command(goto=END)

        logger.info(
            f"check_response verdict=RETRY (retry {new_retry_count}/{self.max_retries}); "
            f"re-entering agent. reason={reason}"
        )
        feedback_text = (
            "Your previous response was judged inadequate by the response analyzer "
            "and the task is not yet complete.\n\n"
            f"Analyzer reason: {reason or '(no reason provided)'}\n\n"
            "Please reconsider the original task, address the issue above, and either "
            "call the appropriate tools to gather more information or produce a corrected, "
            "conclusive final answer."
        )
        feedback_message = HumanMessage(content=feedback_text, name="AnalyzerFeedback")
        return Command(
            update={
                "messages": [feedback_message],
                "retry_count": new_retry_count,
                "agent_prev_node": "check_response",
            },
            goto="agent",
        )

    def invoke(self, inputs, config=None):
        return self.graph.invoke(inputs, config)

    def stream(self, inputs, config=None):
        return self.graph.stream(inputs, config)

    async def astream(
        self,
        inputs: Any,
        stream_mode: Any = "values",
        **kwargs: Any,
    ) -> AsyncIterator[Any]:
        """Async streaming wrapper around the underlying LangGraph compiled graph."""
        async for item in self.graph.astream(
            inputs,
            stream_mode=stream_mode,
            **kwargs,
        ):
            yield item


def context_summary(origin_state, context_trimmer):
    messages = origin_state["messages"]
    if context_trimmer.is_exceeded(messages):
        return context_trimmer.trim(origin_state)
    return origin_state
