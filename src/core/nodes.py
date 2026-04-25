# Copyright (c) 2026 Yunjue Tech
# SPDX-License-Identifier: Apache-2.0
import json
import logging
import os
from typing import Literal

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.runnables import RunnableConfig
from langgraph.types import Command
from pydantic import BaseModel, Field

from src.agents import ReActAgent
from src.config.config import Configuration
from src.prompts.loader import prompt_loader
from src.schema.types import LLMType, State
from src.services.llms.llm import create_llm, get_max_tokens
from src.utils.context_trimmer import ContextTrimmer
from src.utils.utils import load_available_tools

logger = logging.getLogger(__name__)


class GiveAnswerResponse(BaseModel):
    """Structured output aligned with give_answer JSON schema."""

    final_answer: str = Field("", description="Direct answer in required format")
    reasoning_summary: str = Field(
        "",
        description="Brief justification (1-2 sentences) based on findings",
    )


async def react_executor_node(
    state: State, config: RunnableConfig
) -> Command[Literal["integrator", "__end__"]]:
    """Run the ReAct agent and collect the final execution result for the integrator."""
    configurable = Configuration.resolve(config)
    user_query = state.get("user_query", "")

    tools = await load_available_tools(
        configurable.dynamic_tools_dir,
        configurable.dynamic_tools_public_dir,
        user_query,
    )

    tool_names = []
    for tool in tools:
        if hasattr(tool, "name") and tool.name:
            tool_names.append(tool.name)
        elif hasattr(tool, "__name__"):
            tool_names.append(tool.__name__)
        else:
            tool_names.append(str(type(tool).__name__))
    logger.info(f"ReAct tools: {tool_names}")

    default_recursion_limit = int(os.environ.get("MAX_WORKER_RECURSION_LIMIT", 10))
    llm = create_llm(LLMType.BASIC)
    thread_id = (config.get("configurable", {}) or {}).get("thread_id")
    exp_name = (config.get("configurable", {}) or {}).get("exp_name")

    agent = ReActAgent(
        llm,
        tools,
        max_steps=default_recursion_limit,
        user_query=user_query,
        query_id=thread_id,
        exp_name=exp_name,
    )

    task_info = f"# Task\n{user_query}\n"
    agent_input_messages = [HumanMessage(content=task_info)]

    all_messages = []
    final_state = None
    try:
        async for stream_state in agent.astream(
            {
                "messages": agent_input_messages,
                "tool_steps": 0,
                "retry_count": 0,
                "tool_call_cnt": 0,
                "agent_prev_node": "__start__",
            },
            stream_mode="values",
            config={"recursion_limit": 1000},
        ):
            final_state = stream_state
            if isinstance(stream_state, dict) and "messages" in stream_state:
                all_messages = list(stream_state["messages"])
    except Exception as e:
        logger.error(f"Error during ReAct agent stream execution: {e}", exc_info=True)

    tool_call_cnt = 0
    if isinstance(final_state, dict):
        tool_call_cnt = final_state.get("tool_call_cnt", 0)

    execution_res = ""
    if all_messages:
        last_message = all_messages[-1]
        if isinstance(last_message, AIMessage):
            execution_res = last_message.content if isinstance(last_message.content, str) else str(last_message.content)
        else:
            execution_res = str(getattr(last_message, "content", ""))

    logger.info(
        f"ReAct execution finished (result length: {len(execution_res)} chars, tool_calls: {tool_call_cnt})"
    )

    update = {
        "execution_res": execution_res,
        "cumulative_tool_call_cnt": state.get("cumulative_tool_call_cnt", 0) + tool_call_cnt,
    }

    if not execution_res.strip():
        logger.warning("ReAct produced no answer; skipping integrator and ending task.")
        return Command(update={**update, "final_answer": ""}, goto="__end__")

    return Command(update=update, goto="integrator")


async def integrator_node(state: State, config: RunnableConfig):
    """Integrator node that extracts the final answer from the ReAct agent output."""
    logger.info("Using give_answer mode for QA task")
    user_query = state.get("user_query", "")

    system_prompt = prompt_loader.get_prompt(
        "give_answer.md",
        **{"user_query": user_query},
    )
    invoke_messages = [SystemMessage(content=system_prompt)]

    execution_res = state.get("execution_res", "")
    observation_messages = [HumanMessage(content=execution_res, name="Findings")]

    llm_token_limit = get_max_tokens(LLMType.BASIC)
    compressed_state = ContextTrimmer(llm_token_limit).trim({"messages": observation_messages})
    invoke_messages += compressed_state.get("messages", [])

    integrator_llm = create_llm(LLMType.BASIC).with_structured_output(
        GiveAnswerResponse,
        method="json_mode",
    )

    response_content = ""
    structured_payload = None
    try:
        structured_payload = await integrator_llm.ainvoke(invoke_messages)
    except Exception as e:
        logger.error(f"Integrator generation failed: {e}")

    if structured_payload:
        response_content = json.dumps(
            {
                "final_answer": structured_payload.final_answer,
                "reasoning_summary": structured_payload.reasoning_summary,
            },
            ensure_ascii=False,
            indent=2,
        )

    logger.info(f"give_answer response: {response_content}")

    return {
        "final_answer": response_content,
        "cumulative_tool_call_cnt": state.get("cumulative_tool_call_cnt", 0),
    }
