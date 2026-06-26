"""
==================================================
HUMAN REVIEW AGENT

Purpose:
    Wait for human approval before
    continuing the workflow.
==================================================
"""

from langsmith import traceable


@traceable
def human_review_agent(state):

    approval = state.get(
        "approval",
        False
    )

    if approval:

        return {

            "current_agent":
                "memory_agent"
        }

    return {

        "current_agent":
            "teaching_agent",

        "review_comment":
            "Teacher requested explanation improvement."
    }