"""
==================================================
Memory Manager

Purpose:
    Store conversation history

Current Version:
    In-Memory Storage

Future:
    SQLite
    Postgres
    Redis
==================================================
"""


class MemoryManager:

    def __init__(self):

        self.history = []

    def save(self, question, answer):

        self.history.append(
            {
                "question": question,
                "answer": answer
            }
        )

    def get_history(self):

        return self.history