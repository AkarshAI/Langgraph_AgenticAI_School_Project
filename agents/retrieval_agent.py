"""
==================================================
RETRIEVAL AGENT

Purpose:
    Retrieve relevant context from the
    Vector Database (FAISS).

Responsibilities:
    1. Load Vector Database
    2. Create Retriever
    3. Retrieve Similar Chunks
    4. Build Context
    5. Update State

Version:
    RAG
==================================================
"""

from langsmith import traceable

from rag.embedding_model import (
    EmbeddingModel
)

from rag.vector_store import (
    VectorStore
)


@traceable
def retrieval_agent(state):
    """
    Retrieve relevant context
    for the student's question.
    """

    # -------------------------------------------------
    # INPUT
    # -------------------------------------------------

    student_question = state["student_question"]

    # -------------------------------------------------
    # LOAD EMBEDDING MODEL
    # -------------------------------------------------

    embedding_model = EmbeddingModel()

    embeddings = (
        embedding_model.get_embedding_model()
    )

    # -------------------------------------------------
    # LOAD VECTOR DATABASE
    # -------------------------------------------------

    vector_db = VectorStore(
        embeddings
    )

    faiss_db = (
        vector_db.load_vector_store()
    )

    # -------------------------------------------------
    # CREATE RETRIEVER
    # -------------------------------------------------

    retriever = (
        vector_db.get_retriever(
            faiss_db,
            k=3
        )
    )

    # -------------------------------------------------
    # RETRIEVE DOCUMENTS
    # -------------------------------------------------

    documents = retriever.invoke(
        student_question
    )

    # -------------------------------------------------
    # BUILD CONTEXT
    # -------------------------------------------------

    retrieved_chunks = []

    context = ""

    for document in documents:

        retrieved_chunks.append(
            document.page_content
        )

        context += (
            document.page_content
            + "\n\n"
        )

    # -------------------------------------------------
    # UPDATE STATE
    # -------------------------------------------------

    return {

        "current_agent":
            "teaching_agent",

        "vector_store":
            faiss_db,

        "retriever":
            retriever,

        "retrieved_chunks":
            retrieved_chunks,

        "context":
            context
    }