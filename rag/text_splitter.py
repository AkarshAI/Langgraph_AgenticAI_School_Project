"""
==================================================
TEXT SPLITTER

Purpose:
    Split large documents into smaller chunks
    before generating embeddings.

Version:
    RAG
==================================================
"""

from langchain.text_splitter import (
    RecursiveCharacterTextSplitter
)


class TextSplitter:

    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 100
    ):

        self.splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
                length_function=len,
                separators=[
                    "\n\n",
                    "\n",
                    ". ",
                    " ",
                    ""
                ]
            )
        )

    # -------------------------------------------------
    # SPLIT DOCUMENTS
    # -------------------------------------------------

    def split_documents(
        self,
        documents
    ):

        chunks = self.splitter.split_documents(
            documents
        )

        return chunks

    # -------------------------------------------------
    # SPLIT RAW TEXT
    # -------------------------------------------------

    def split_text(
        self,
        text: str
    ):

        chunks = self.splitter.split_text(
            text
        )

        return chunks