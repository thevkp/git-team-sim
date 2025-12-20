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
      status TEXT NOT NULL,
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
  
  cur.execute("SELECT id, description, status, created_at FROM tasks")
  rows = cur.fetchall()
  
  conn.close()
  return rows

def update_status(task_id):
  conn = get_connection()
  cur = conn.cursor()
        
  cur.execute(
    "UPDATE tasks SET status = ? WHERE id = ?",
    ("completed", task_id)
  )
  
  conn.commit()
  
  if cur.rowcount == 0:
    conn.close()
    return False #nothin updated
  else:
    conn.close()
    return True
  
def get_tasks_by_status(status):
  conn = get_connection()
  cur = conn.cursor()
  
  cur.execute(
    """SELECT id, description, status, created_at FROM
    tasks WHERE status = ? ORDER BY id""", (status,)
  )
  
  tasks = cur.fetchall()
  conn.close()
  return tasks
  pass
  
def delete_task(task_id):
  conn = get_connection()
  cur = conn.cursor()
  
  cur.execute(
    "DELETE FROM tasks WHERE id = ?", (task_id,)
  )
  
  conn.commit()
  
  if cur.rowcount == 0:
    conn.close()
    return False #Nothing deleted
  else:
    conn.close()
    return True
  
def delete_tasks_by_status(status):
  conn = get_connection()
  cur = conn.cursor()
  
  cur.execute("DELETE FROM tasks WHERE status = ?", (status))
  
  conn.commit()
  
  if cur.rowcount == 0:
    conn.close()
    return False
  else:
    conn.close()
    return True