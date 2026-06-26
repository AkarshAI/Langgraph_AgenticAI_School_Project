from langsmith import traceable

from prompts.quiz_prompt import (
    QUIZ_PROMPT,
    ANSWER_PROMPT
)


@traceable
def quiz_agent(state):

    llm = state["llm"]

    topic = state["topic"]

    quiz_prompt = QUIZ_PROMPT.format(
        topic=topic
    )

    quiz_question = llm.invoke(
        quiz_prompt
    ).content

    answer_prompt = ANSWER_PROMPT.format(
        topic=topic
    )

    correct_answer = llm.invoke(
        answer_prompt
    ).content

    return {

        "current_agent":
            "evaluation_agent",

        "quiz":
            [quiz_question],

        "correct_answer":
            correct_answer
    }