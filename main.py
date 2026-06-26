"""
==================================================
MAIN APPLICATION

Government School Learning Assistant

Version 6
Multi-Agent Architecture

Agents:
1. Supervisor Agent
2. Teaching Agent
3. Quiz Agent
4. Evaluation Agent
5. Memory Agent
6. Report Agent
==================================================
"""

from langchain_openai import ChatOpenAI

from graphs.supervisor_graph import (
    supervisor_graph
)

from memory.memory_manager import (
    MemoryManager
)

from rag.embedding_model import (
    EmbeddingModel
)

from rag.vector_store import (
    VectorStore
)
config = {

    "configurable": {

        "thread_id":
            "student_001"
    }
}
# ==================================================
# LLM CONFIGURATION
# ==================================================

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# ==================================================
# EMBEDDING MODEL
# ==================================================

embedding_model = EmbeddingModel()

embeddings = (
    embedding_model.get_embedding_model()
)

# ==================================================
# VECTOR DATABASE
# ==================================================

vector_store = VectorStore(
    embeddings
)

faiss_db = (
    vector_store.load_vector_store()
)

retriever = (
    vector_store.get_retriever(
        faiss_db,
        k=3
    )
)

# ==================================================
# MEMORY
# ==================================================

memory = MemoryManager()

# ==================================================
# STUDENT INPUT
# ==================================================

student_question = (
    "What is photosynthesis?"
)

student_answer = (
    "Photosynthesis"
)

# ==================================================
# EXECUTE GRAPH
# ==================================================

result = supervisor_graph.invoke(
    {

        "llm":
            llm,

        "memory":
            memory,

        "retriever":
            retriever,

        "vector_store":
            faiss_db,

        "student_question":
            student_question,

        "student_answer":
            student_answer,

        "approval":
            True

    },
    config=config
)

# ==================================================
# QUESTION
# ==================================================

print("\n" + "=" * 50)
print("QUESTION")
print("=" * 50)

print(
    result["student_question"]
)

# ==================================================
# RETRIEVED CONTEXT
# ==================================================

print("\n" + "=" * 50)
print("RETRIEVED CHUNKS")
print("=" * 50)

for i, chunk in enumerate(
    result["retrieved_chunks"],
    start=1
):

    print(f"\nChunk {i}")

    print("-" * 50)

    print(chunk)

# ==================================================
# CONTEXT
# ==================================================

print("\n" + "=" * 50)
print("CONTEXT")
print("=" * 50)

print(
    result["context"]
)
# ==================================================
# TOPIC
# ==================================================

print("\n" + "=" * 50)
print("TOPIC")
print("=" * 50)

print(
    result["topic"]
)

# ==================================================
# EXPLANATION
# ==================================================

print("\n" + "=" * 50)
print("EXPLANATION")
print("=" * 50)

print(
    result["explanation"]
)

# ==================================================
# QUIZ
# ==================================================

print("\n" + "=" * 50)
print("QUIZ")
print("=" * 50)

for question in result["quiz"]:

    print(question)

# ==================================================
# STUDENT ANSWER
# ==================================================

print("\n" + "=" * 50)
print("STUDENT ANSWER")
print("=" * 50)

print(
    result["student_answer"]
)

# ==================================================
# CORRECT ANSWER
# ==================================================

print("\n" + "=" * 50)
print("CORRECT ANSWER")
print("=" * 50)

print(
    result["correct_answer"]
)

# ==================================================
# SCORE
# ==================================================

print("\n" + "=" * 50)
print("SCORE")
print("=" * 50)

print(
    result["score"]
)

# ==================================================
# FEEDBACK
# ==================================================

print("\n" + "=" * 50)
print("FEEDBACK")
print("=" * 50)

print(
    result["feedback"]
)

# ==================================================
# MEMORY HISTORY
# ==================================================

print("\n" + "=" * 50)
print("MEMORY HISTORY")
print("=" * 50)

for item in result["history"]:

    print(item)

# ==================================================
# TEACHER REPORT
# ==================================================

print("\n" + "=" * 50)
print("TEACHER REPORT")
print("=" * 50)

report = result["teacher_report"]

print(
    f"Total Questions : "
    f"{report['total_questions']}"
)

print(
    f"Correct Answers : "
    f"{report['correct_answers']}"
)

print(
    f"Accuracy : "
    f"{report['accuracy']}%"
)

print(
    f"Average Score : "
    f"{report['average_score']}"
)

print(
    f"Performance : "
    f"{report['performance']}"
)

# ==================================================
# WORKFLOW STATUS
# ==================================================

print("\n" + "=" * 50)
print("WORKFLOW STATUS")
print("=" * 50)

print(
    result["current_agent"]
)

# ==================================================
# COMPLETED
# ==================================================

print("\n" + "=" * 50)
print("MULTI-AGENT WORKFLOW COMPLETED")
print("=" * 50)