# Copyright (c) 2026 Yunjue Tech
# SPDX-License-Identifier: Apache-2.0
from langgraph.graph import END, START, StateGraph

from src.schema.types import State

from .nodes import integrator_node, react_executor_node


def build_graph():
    builder = StateGraph(State)
    builder.add_node("react_executor", react_executor_node)
    builder.add_node("integrator", integrator_node)
    builder.add_edge(START, "react_executor")
    builder.add_edge("integrator", END)
    return builder
