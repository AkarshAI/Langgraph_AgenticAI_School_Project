from langsmith import traceable


@traceable
def supervisor_agent(state):

    return {

        "current_agent":
            "teaching_agent"
    }