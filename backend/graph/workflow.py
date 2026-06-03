# graph/workflow.py
from langgraph.graph import StateGraph, END
from schemas.state import WorkflowState

# Import the updated nodes
from graph.nodes import (
    project_manager_node,
    architect_node,
    implement_node,
    qa_node,
    report_node
)

# Initialize the state-driven workflow graph
workflow = StateGraph(WorkflowState)

# 1. Add Nodes
workflow.add_node("project_manager", project_manager_node)
workflow.add_node("architect", architect_node)
workflow.add_node("implementation", implement_node)  # Consolidated node
workflow.add_node("qa", qa_node)
workflow.add_node("report", report_node)

# 2. Define Flow Routing (Entry points & Edges)
workflow.set_entry_point("project_manager")

workflow.add_edge("project_manager", "architect")
workflow.add_edge("architect", "implementation")  # Route directly into fullstack
workflow.add_edge("implementation", "qa")         # Route directly out to QA
workflow.add_edge("qa", "report")
workflow.add_edge("report", END)

# Compile graph application
app = workflow.compile()