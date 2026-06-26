from langsmith import traceable

from prompts.explain_prompt import (
    EXPLAIN_PROMPT
)

@traceable
def explain_concept(state):

    llm = state["llm"]

    topic = state["topic"]

    prompt = EXPLAIN_PROMPT.format(
        topic=topic
    )

    explanation = llm.invoke(prompt).content

    return {
        "explanation": explanation
    }