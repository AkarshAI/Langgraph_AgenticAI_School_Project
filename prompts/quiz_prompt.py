from langchain_core.prompts import (
    ChatPromptTemplate
)

QUIZ_PROMPT = ChatPromptTemplate.from_template(
    """
    Create one quiz question for:

    {topic}

    Return only question.
    """
)

ANSWER_PROMPT = ChatPromptTemplate.from_template(
    """
    Generate answer for:

    {topic}

    Return short answer.
    """
)