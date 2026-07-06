from langgraph.graph import StateGraph

from graph.state import WorkflowState

from graph.node import (
    website_node,
    brd_node,
    requirement_node,
)

builder = StateGraph(WorkflowState)

builder.add_node(
    "website",
    website_node
)

builder.add_node(
    "brd",
    brd_node
)

builder.add_node(
    "requirements",
    requirement_node
)

builder.set_entry_point(
    "website"
)

builder.add_edge(
    "website",
    "brd"
)

builder.add_edge(
    "brd",
    "requirements"
)

builder.set_finish_point(
    "requirements"
)

graph = builder.compile()