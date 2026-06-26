from langsmith import traceable

from prompts.react_prompt import (
    REACT_PROMPT
)

from tools.calculator_tool import (
    calculator_tool
)

from tools.search_tool import (
    search_tool
)


@traceable
def react_agent(state):

    llm = state["llm"]

    question = (
        state["student_question"]
    )

    llm_with_tools = (
        llm.bind_tools(
            [
                calculator_tool,
                search_tool
            ]
        )
    )

    prompt = (
        REACT_PROMPT.format(
            question=question
        )
    )

    response = (
        llm_with_tools.invoke(
            prompt
        )
    )

    return {

        "tool_result":
            response.content,

        "current_agent":
            "memory_agent"
    }