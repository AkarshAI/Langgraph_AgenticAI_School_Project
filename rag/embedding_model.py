"""
==================================================
EMBEDDING MODEL

Purpose:
    Generate vector embeddings for text chunks.

Version:
    RAG
==================================================
"""

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)


class EmbeddingModel:

    def __init__(
        self,
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
    ):

        self.embeddings = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs={
                "device": "cpu"
            },
            encode_kwargs={
                "normalize_embeddings": True
            }
        )

    # -------------------------------------------------
    # RETURN EMBEDDING MODEL
    # -------------------------------------------------

    def get_embedding_model(self):

        return self.embeddings

    # -------------------------------------------------
    # EMBED SINGLE QUERY
    # -------------------------------------------------

    def embed_query(
        self,
        query: str
    ):

        return self.embeddings.embed_query(
            query
        )

    # -------------------------------------------------
    # EMBED MULTIPLE DOCUMENTS
    # -------------------------------------------------

    def embed_documents(
        self,
        documents: list[str]
    ):

        return self.embeddings.embed_documents(
            documents
        )