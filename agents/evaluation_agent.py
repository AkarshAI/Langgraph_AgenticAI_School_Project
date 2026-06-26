from langsmith import traceable


@traceable
def evaluation_agent(state):

    student_answer = (
        state["student_answer"]
        .strip()
        .lower()
    )

    correct_answer = (
        state["correct_answer"]
        .strip()
        .lower()
    )

    if student_answer == correct_answer:

        score = 100

        feedback = (
            "Correct Answer"
        )

    else:

        score = 0

        feedback = (
            f"Incorrect Answer. "
            f"Expected: {correct_answer}"
        )

    return {

        "current_agent":
            "memory_agent",

        "score":
            score,

        "feedback":
            feedback
    }