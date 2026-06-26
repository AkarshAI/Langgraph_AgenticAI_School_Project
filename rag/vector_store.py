"""
==================================================
VECTOR STORE

Purpose:
    Create, Save and Load
    FAISS Vector Database.

Version:
    RAG
==================================================
"""

from pathlib import Path

from langchain_community.vectorstores import (
    FAISS
)


class VectorStore:

    def __init__(
        self,
        embeddings
    ):

        self.embeddings = embeddings

    # -------------------------------------------------
    # CREATE VECTOR DATABASE
    # -------------------------------------------------

    def create_vector_store(
        self,
        chunks
    ):

        vector_store = FAISS.from_documents(
            documents=chunks,
            embedding=self.embeddings
        )

        return vector_store

    # -------------------------------------------------
    # SAVE VECTOR DATABASE
    # -------------------------------------------------

    def save_vector_store(
        self,
        vector_store,
        save_path: str = "vector_db"
    ):

        Path(save_path).mkdir(
            parents=True,
            exist_ok=True
        )

        vector_store.save_local(
            save_path
        )

        print(
            f"\nVector Database saved to : {save_path}"
        )

    # -------------------------------------------------
    # LOAD VECTOR DATABASE
    # -------------------------------------------------

    def load_vector_store(
        self,
        save_path: str = "vector_db"
    ):

        vector_store = FAISS.load_local(

            folder_path=save_path,

            embeddings=self.embeddings,

            allow_dangerous_deserialization=True
        )

        return vector_store

    # -------------------------------------------------
    # CREATE RETRIEVER
    # -------------------------------------------------

    def get_retriever(

        self,

        vector_store,

        search_type: str = "similarity",

        k: int = 3

    ):

        retriever = vector_store.as_retriever(

            search_type=search_type,

            search_kwargs={
                "k": k
            }

        )

        return retriever