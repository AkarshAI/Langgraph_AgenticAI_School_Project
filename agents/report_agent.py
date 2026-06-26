from langsmith import traceable


@traceable
def report_agent(state):

    history = state["history"]

    total_questions = len(history)

    correct_answers = 0

    total_score = 0

    for item in history:

        total_score += item["score"]

        if item["score"] == 100:

            correct_answers += 1

    accuracy = 0
    average_score = 0

    if total_questions > 0:

        accuracy = (
            correct_answers /
            total_questions
        ) * 100

        average_score = (
            total_score /
            total_questions
        )

    if accuracy >= 80:

        performance = "Excellent"

    elif accuracy >= 60:

        performance = "Good"

    elif accuracy >= 40:

        performance = "Average"

    else:

        performance = "Needs Improvement"

    teacher_report = {

        "total_questions":
            total_questions,

        "correct_answers":
            correct_answers,

        "accuracy":
            round(accuracy, 2),

        "average_score":
            round(average_score, 2),

        "performance":
            performance
    }

    return {

        "current_agent":
            "workflow_completed",

        "teacher_report":
            teacher_report
    }