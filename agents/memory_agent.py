from langsmith import traceable


@traceable
def memory_agent(state):

    memory = state["memory"]

    record = {

        "question":
            state["student_question"],

        "student_answer":
            state["student_answer"],

        "correct_answer":
            state["correct_answer"],

        "score":
            state["score"],

        "feedback":
            state["feedback"]
    }

    memory.save(record)

    history = memory.get_history()

    return {

        "current_agent":
            "report_agent",

        "history":
            history
    }