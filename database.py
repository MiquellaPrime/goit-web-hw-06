import sqlite3
from contextlib import contextmanager

DATABASE_PATH = "./university.db"


@contextmanager
def create_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    try:
        yield conn
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
