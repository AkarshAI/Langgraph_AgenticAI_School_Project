from langchain_core.prompts import (
    ChatPromptTemplate
)

TOPIC_PROMPT = ChatPromptTemplate.from_template(
    """
    Identify topic from question.

    Question:
    {question}

    Return only topic name.
    """
)

EXPLANATION_PROMPT = ChatPromptTemplate.from_template(
    """
    Explain the topic to a government school student.

    Topic:
    {topic}

    Use simple language.
    """
)