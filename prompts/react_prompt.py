from langchain_core.prompts import (
    ChatPromptTemplate
)

REACT_PROMPT = ChatPromptTemplate.from_template(
    """
    You are a ReAct Agent.

    Question:
    {question}

    Think step by step.

    If needed use tools.

    Generate final answer.
    """
)