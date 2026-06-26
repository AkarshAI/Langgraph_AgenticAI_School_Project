"""
==========================================================
PROJECT: Government School Learning Assistant
PURPOSE:
    Learn LangChain + LangGraph + Pydantic + LangSmith

CURRENT VERSION:
    Simple Single File Prototype

FUTURE:
    Can be expanded into production architecture
==========================================================
"""

# ==========================================================
# IMPORTS
# ==========================================================

from typing import TypedDict, List

from pydantic import BaseModel, Field

from langchain_openai import ChatOpenAI

from langgraph.graph import StateGraph, START, END

from langsmith import traceable


# ==========================================================
# LANGSMITH CONFIGURATION
# ==========================================================

"""
Set Environment Variables

LANGCHAIN_API_KEY=xxxxx
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=GovtSchoolAgent

These help visualize graph execution in LangSmith.
"""


# ==========================================================
# LLM CONFIGURATION
# ==========================================================

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# ==========================================================
# PYDANTIC MODELS
# ==========================================================

class StudentQuestion(BaseModel):
    """
    Structured understanding of student question.
    """

    question: str = Field(..., description="Student question")
    topic: str = Field(..., description="Detected topic")


class QuizQuestion(BaseModel):
    """
    Quiz generated for student.
    """

    question: str
    answer: str


# ==========================================================
# LANGGRAPH STATE
# ==========================================================

class LearningState(TypedDict):
    """
    State shared between all nodes.
    """

    student_question: str

    topic: str

    explanation: str

    examples: List[str]

    quiz: List[str]


# ==========================================================
# NODE 1
# UNDERSTAND QUESTION
# ==========================================================

@traceable
def understand_question(state: LearningState):

    question = state["student_question"]

    prompt = f"""
    Identify topic from question.

    Question:
    {question}

    Return only topic name.
    """

    topic = llm.invoke(prompt).content

    return {
        "topic": topic
    }


# ==========================================================
# NODE 2
# EXPLAIN CONCEPT
# ==========================================================

@traceable
def explain_concept(state: LearningState):

    topic = state["topic"]

    prompt = f"""
    Explain {topic}
    for government school student.

    Use simple language.
    """

    explanation = llm.invoke(prompt).content

    return {
        "explanation": explanation
    }


# ==========================================================
# NODE 3
# GENERATE EXAMPLES
# ==========================================================

@traceable
def generate_examples(state: LearningState):

    topic = state["topic"]

    prompt = f"""
    Give 3 simple examples of:

    {topic}
    """

    response = llm.invoke(prompt).content

    examples = response.split("\n")

    return {
        "examples": examples
    }


# ==========================================================
# NODE 4
# GENERATE QUIZ
# ==========================================================

@traceable
def generate_quiz(state: LearningState):

    topic = state["topic"]

    prompt = f"""
    Generate 3 quiz questions on:

    {topic}
    """

    quiz = llm.invoke(prompt).content

    return {
        "quiz": [quiz]
    }


# ==========================================================
# BUILD LANGGRAPH
# ==========================================================

graph_builder = StateGraph(LearningState)

graph_builder.add_node(
    "understand_question",
    understand_question
)

graph_builder.add_node(
    "explain_concept",
    explain_concept
)

graph_builder.add_node(
    "generate_examples",
    generate_examples
)

graph_builder.add_node(
    "generate_quiz",
    generate_quiz
)

# ==========================================================
# EDGES
# ==========================================================

graph_builder.add_edge(
    START,
    "understand_question"
)

graph_builder.add_edge(
    "understand_question",
    "explain_concept"
)

graph_builder.add_edge(
    "explain_concept",
    "generate_examples"
)

graph_builder.add_edge(
    "generate_examples",
    "generate_quiz"
)

graph_builder.add_edge(
    "generate_quiz",
    END
)

# ==========================================================
# COMPILE GRAPH
# ==========================================================

graph = graph_builder.compile()

# ==========================================================
# EXECUTION
# ==========================================================

if __name__ == "__main__":

    result = graph.invoke(
        {
            "student_question":
                "What is photosynthesis?"
        }
    )

    print("\nTOPIC")
    print(result["topic"])

    print("\nEXPLANATION")
    print(result["explanation"])

    print("\nEXAMPLES")
    print(result["examples"])

    print("\nQUIZ")
    print(result["quiz"])