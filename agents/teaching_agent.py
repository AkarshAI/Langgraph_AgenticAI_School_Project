from langsmith import traceable

from prompts.teaching_prompt import (
    TOPIC_PROMPT,
    EXPLANATION_PROMPT
)

from tools.calculator_tool import (
    calculator_tool
)

from tools.search_tool import (
    search_tool
)


@traceable
def teaching_agent(state):

    llm = state["llm"]

    tools = [

        calculator_tool,

        search_tool
    ]

    llm_with_tools = (
        llm.bind_tools(
            tools
        )
    )

    student_question = (
        state["student_question"]
    )

    topic_prompt = TOPIC_PROMPT.format(
        question=student_question
    )

    topic = llm.invoke(
        topic_prompt
    ).content

    explanation_prompt = (
        EXPLANATION_PROMPT.format(
            topic=topic
        )
    )

    response = (
        llm_with_tools.invoke(
            explanation_prompt
        )
    )

    explanation = (
        response.content
    )

    return {

        "current_agent":
            "quiz_agent",

        "topic":
            topic,

        "explanation":
            explanation
    }