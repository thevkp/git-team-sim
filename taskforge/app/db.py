import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data"/"taskforge.db"

def get_connection():
  return sqlite3.connect(DB_PATH)

def init_db():
  conn = get_connection()
  cur = conn.cursor()
  
  
  cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      description TEXT NOT NULL,
      status TExT NOT NULL,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )       
  """)
  
  conn.commit()
  conn.close()
  
def add_task(description: str):
  conn = get_connection()
  cur = conn.cursor()
  cur.execute(
    "INSERT INTO tasks (description, status) VALUES(?, ?)", 
    (description, "pending")
  )
  
  conn.commit()
  conn.close()
  
  
def list_tasks():
  conn = sqlite3.connect(DB_PATH)
  cur = conn.cursor()
  
  cur.execute("SELECT id, description FROM tasks")
  rows = cur.fetchall()
  
  conn.close()
  return rows