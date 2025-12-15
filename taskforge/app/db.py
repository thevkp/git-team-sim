import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data"/"taskforge.db"

def get_connection():
  return sqlite3.connect(DB_PATH)

def init_db():
  conn = get_connection()
  cursor = conn.cursor()
  
  
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      description TEXT NOT NULL,
      status TExT NOT NULL,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )       
  """)
  
  conn.commit()
  conn.close()