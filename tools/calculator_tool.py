from langchain.tools import tool


@tool
def calculator_tool(
    expression: str
) -> str:
    """
    Perform mathematical calculations.
    """

    try:

        result = eval(
            expression
        )

        return str(result)

    except Exception as e:

        return (
            f"Error: {str(e)}"
        )