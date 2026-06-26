from langsmith import traceable

from prompts.example_prompt import (
    EXAMPLE_PROMPT
)

@traceable
def generate_examples(state):

    llm = state["llm"]

    topic = state["topic"]

    prompt = EXAMPLE_PROMPT.format(
        topic=topic
    )

    response = llm.invoke(prompt).content

    return {
        "examples": response.split("\n")
    }