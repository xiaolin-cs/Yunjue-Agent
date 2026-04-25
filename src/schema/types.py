# Copyright (c) 2026 Yunjue Tech
# SPDX-License-Identifier: Apache-2.0
from enum import Enum
from typing import Any, Dict, Optional

from langgraph.graph import MessagesState
from pydantic import BaseModel, Field


class LLMType(Enum):
    BASIC = "basic"
    VISION = "vision"
    SUMMARIZE = "summarize"
    TOOL_ANALYZE = "tool_analyze"


class ResponseAnalysis(BaseModel):
    """Verdict produced by the response analyzer agent."""

    status: str = Field(
        "RETRY",
        description="Overall verdict: FINISH when the worker response is conclusive, otherwise RETRY.",
    )
    reason: str = Field(
        "",
        description="Short explanation of why the response was judged FINISH or RETRY.",
    )


class ToolExecutionRecord(BaseModel):
    tool_name: str
    caller_message_id: str
    tool_message_id: str = ""
    tool_call_id: str
    arguments: Dict[str, Any]
    result: Optional[Any] = None
    error: Optional[str] = None


class State(MessagesState):
    user_query: str = ""
    final_answer: str = ""
    execution_res: str = ""

    cumulative_tool_call_cnt: int = 0
