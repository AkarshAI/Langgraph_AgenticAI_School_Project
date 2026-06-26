from langchain_core.prompts import (
    ChatPromptTemplate
)

FEEDBACK_PROMPT = ChatPromptTemplate.from_template(
    """
    Student Answer:
    {student_answer}

    Correct Answer:
    {correct_answer}

    Generate feedback.
    """
)