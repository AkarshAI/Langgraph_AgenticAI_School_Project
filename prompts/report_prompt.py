from langchain_core.prompts import (
    ChatPromptTemplate
)

REPORT_PROMPT = ChatPromptTemplate.from_template(
    """
    Generate teacher report.

    Accuracy:
    {accuracy}

    Performance:
    {performance}
    """
)