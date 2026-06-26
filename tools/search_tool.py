from langchain.tools import tool


@tool
def search_tool(
    query: str
) -> str:
    """
    Search educational content.
    """

    return (
        f"Search Result for: {query}"
    )