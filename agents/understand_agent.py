from langsmith import traceable

from prompts.understand_prompt import (
    UNDERSTAND_PROMPT
)

@traceable
def understand_question(state):

    llm = state["llm"]

    question = state["student_question"]

    prompt = UNDERSTAND_PROMPT.format(
        question=question
    )

    topic = llm.invoke(prompt).content

    return {
        "topic": topic
    }