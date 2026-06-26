"""
==================================================
RAG INGESTION PIPELINE

Purpose:
    1. Load documents
    2. Split documents
    3. Generate embeddings
    4. Create FAISS Vector Database
    5. Save Vector Database

Run Once

python rag/ingest.py
==================================================
"""

from pathlib import Path

from rag.document_loader import (
    DocumentLoader
)

from rag.text_splitter import (
    TextSplitter
)

from rag.embedding_model import (
    EmbeddingModel
)

from rag.vector_store import (
    VectorStore
)


class RAGIngestionPipeline:

    def __init__(self):

        self.loader = DocumentLoader()

        self.splitter = TextSplitter()

        self.embedding_model = EmbeddingModel()

        self.embeddings = (
            self.embedding_model.get_embedding_model()
        )

        self.vector_store = VectorStore(
            self.embeddings
        )

    # -------------------------------------------------
    # INGEST DOCUMENTS
    # -------------------------------------------------

    def ingest(
        self,
        file_paths: list[str]
    ):

        print("\nLoading documents...")

        documents = self.loader.load_documents(
            file_paths
        )

        print(
            f"Loaded {len(documents)} document(s)"
        )

        # ---------------------------------------------

        print("\nSplitting documents...")

        chunks = self.splitter.split_documents(
            documents
        )

        print(
            f"Generated {len(chunks)} chunks"
        )

        # ---------------------------------------------

        print("\nCreating FAISS Vector Database...")

        faiss_db = (
            self.vector_store.create_vector_store(
                chunks
            )
        )

        # ---------------------------------------------

        print("\nSaving Vector Database...")

        self.vector_store.save_vector_store(
            faiss_db
        )

        print("\nRAG Ingestion Completed Successfully.")

        return faiss_db


# ==================================================
# MAIN
# ==================================================

if __name__ == "__main__":

    DATA_FOLDER = Path("data")

    supported_extensions = {
        ".pdf",
        ".docx",
        ".txt"
    }

    files = []

    for file in DATA_FOLDER.iterdir():

        if (
            file.is_file()
            and file.suffix.lower()
            in supported_extensions
        ):

            files.append(
                str(file)
            )

    if not files:

        print(
            "\nNo supported documents found in data/ folder."
        )

    else:

        pipeline = (
            RAGIngestionPipeline()
        )

        pipeline.ingest(
            files
        )