from langgraph.graph import (
    StateGraph,
    START,
    END
)

from models.states import LearningState


from agents.quiz_agent import generate_quiz
from agents.evaluation_agent import evaluation_agent
from agents.memory_agent import memory_agent
from agents.report_agent import report_agent


graph_builder = StateGraph(
    LearningState
)

# ==================================================
# NODES
# ==================================================

graph_builder.add_node(
    "router",
    router_agent
)

graph_builder.add_node(
    "math_agent",
    math_agent
)

graph_builder.add_node(
    "science_agent",
    science_agent
)

graph_builder.add_node(
    "general_agent",
    general_agent
)

graph_builder.add_node(
    "generate_quiz",
    generate_quiz
)

graph_builder.add_node(
    "evaluation_agent",
    evaluation_agent
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

def route_decision(state):

    return state["route"]


# ==================================================
# START
# ==================================================

graph_builder.add_edge(
    START,
    "router"
)

# ==================================================
# CONDITIONAL EDGES
# ==================================================

graph_builder.add_conditional_edges(
    "router",
    route_decision,
    {
        "math": "math_agent",
        "science": "science_agent",
        "general": "general_agent"
    }
)

# ==================================================
# SUBJECT AGENTS
# ==================================================

graph_builder.add_edge(
    "math_agent",
    "generate_quiz"
)

graph_builder.add_edge(
    "science_agent",
    "generate_quiz"
)

graph_builder.add_edge(
    "general_agent",
    "generate_quiz"
)

# ==================================================
# QUIZ FLOW
# ==================================================

graph_builder.add_edge(
    "generate_quiz",
    "evaluation_agent"
)

graph_builder.add_edge(
    "evaluation_agent",
    "memory_agent"
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

learning_graph = graph_builder.compile()