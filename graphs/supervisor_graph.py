"""
==================================================
SUPERVISOR GRAPH

Version 12

Workflow

START
  │
  ▼
Supervisor Agent
  │
  ▼
Retrieval Agent
  │
  ▼
Teaching Agent
  │
  ▼
ReAct Agent
  │
  ▼
Quiz Agent
  │
  ▼
Evaluation Agent
  │
  ▼
Human Review Agent
  │
  ├─────────────► Reject
  │                 │
  │                 ▼
  │          Teaching Agent
  │
  └─────────────► Approve
                    │
                    ▼
               Memory Agent
                    │
                    ▼
               Report Agent
                    │
                    ▼
                   END
==================================================
"""

from langgraph.graph import (
    StateGraph,
    START,
    END
)

from models.states import LearningState

from agents.supervisor_agent import supervisor_agent
from agents.retrieval_agent import retrieval_agent
from agents.teaching_agent import teaching_agent
from agents.react_agent import react_agent
from agents.quiz_agent import quiz_agent
from agents.evaluation_agent import evaluation_agent
from agents.human_review_agent import human_review_agent
from agents.memory_agent import memory_agent
from agents.report_agent import report_agent

from memory.checkpointer import checkpointer

# ==================================================
# CREATE GRAPH
# ==================================================

graph_builder = StateGraph(
    LearningState
)

# ==================================================
# REGISTER NODES
# ==================================================

graph_builder.add_node(
    "supervisor_agent",
    supervisor_agent
)

graph_builder.add_node(
    "retrieval_agent",
    retrieval_agent
)

graph_builder.add_node(
    "teaching_agent",
    teaching_agent
)

graph_builder.add_node(
    "react_agent",
    react_agent
)

graph_builder.add_node(
    "quiz_agent",
    quiz_agent
)

graph_builder.add_node(
    "evaluation_agent",
    evaluation_agent
)

graph_builder.add_node(
    "human_review_agent",
    human_review_agent
)

graph_builder.add_node(
    "memory_agent",
    memory_agent
)

graph_builder.add_node(
    "report_agent",
    report_agent
)

# ==================================================
# ROUTER
# ==================================================

def approval_router(state):

    if state.get("approval", False):

        return "approved"

    return "rejected"

# ==================================================
# EDGES
# ==================================================

graph_builder.add_edge(
    START,
    "supervisor_agent"
)

graph_builder.add_edge(
    "supervisor_agent",
    "retrieval_agent"
)

graph_builder.add_edge(
    "retrieval_agent",
    "teaching_agent"
)

graph_builder.add_edge(
    "teaching_agent",
    "react_agent"
)

graph_builder.add_edge(
    "react_agent",
    "quiz_agent"
)

graph_builder.add_edge(
    "quiz_agent",
    "evaluation_agent"
)

graph_builder.add_edge(
    "evaluation_agent",
    "human_review_agent"
)

graph_builder.add_conditional_edges(
    "human_review_agent",
    approval_router,
    {
        "approved": "memory_agent",
        "rejected": "teaching_agent"
    }
)

graph_builder.add_edge(
    "memory_agent",
    "report_agent"
)

graph_builder.add_edge(
    "report_agent",
    END
)

# ==================================================
# COMPILE
# ==================================================

supervisor_graph = graph_builder.compile(
    checkpointer=checkpointer
)