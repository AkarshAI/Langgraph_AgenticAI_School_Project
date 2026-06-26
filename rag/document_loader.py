"""
==================================================
DOCUMENT LOADER

Purpose:
    Load documents for RAG.

Supported Formats:
    - PDF
    - DOCX
    - TXT

Version:
    RAG
==================================================
"""

from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader
)


class DocumentLoader:

    def __init__(self):

        pass

    # -------------------------------------------------
    # LOAD SINGLE DOCUMENT
    # -------------------------------------------------

    def load_document(
        self,
        file_path: str
    ):

        file_path = Path(file_path)

        extension = (
            file_path.suffix.lower()
        )

        if extension == ".pdf":

            loader = PyPDFLoader(
                str(file_path)
            )

        elif extension == ".txt":

            loader = TextLoader(
                str(file_path),
                encoding="utf-8"
            )

        elif extension == ".docx":

            loader = Docx2txtLoader(
                str(file_path)
            )

        else:

            raise ValueError(
                f"Unsupported file format: {extension}"
            )

        documents = loader.load()

        return documents

    # -------------------------------------------------
    # LOAD MULTIPLE DOCUMENTS
    # -------------------------------------------------

    def load_documents(
        self,
        file_paths: list[str]
    ):

        all_documents = []

        for file_path in file_paths:

            documents = self.load_document(
                file_path
            )

            all_documents.extend(
                documents
            )

        return all_documents