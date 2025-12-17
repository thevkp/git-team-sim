import sys
# from app.db import init_db, add_task, list_tasks, update_status, delete_task
from app.db import *


def main():
  init_db()
  
  if len(sys.argv) < 2: 
    print("Usage:")
    print("   python main.py add \"task description\"")
    print("   python main.py list")
    print("   python main.py update task_id")
    return 
  
  command = sys.argv[1].lower()
  
  if command == "add":
    if len(sys.argv) < 3:
      print("Error: Task description is missing.")
      print("Usage: python -m main.py add \"task description\"")
      return
    
    # Join all remaining args in case the description has spaces
    description = " ".join(sys.argv[2:])
    add_task(description)
    print(f"Task added: {description}")
    
  elif command == "list":
    tasks = list_tasks()
    if not tasks:
      print("No tasks found")
    else:
      print("Tasks: ")
      for task_id, desc, status, created_at in tasks:
        print(f"{task_id}. Description  : {desc}")
        print(f"   status       : {status}")
        print(f"   Created At   : {created_at}")
        print("-" * 40)
    
  elif command == "update":
    if len(sys.argv) < 3:
      print("Error: Task id is missing.")
      print("Usage: python -m main.py update \"task_id\"")
      return
    
    try:
      task_id = int(sys.argv[2])
    except ValueError:
      print("Error: Task id must be a number.")
      return

    success = update_status(task_id)
    if success:
      print(f"status updated for task ID: {task_id}")
    else:
      print(f"No task found with ID: {task_id}")
  
  elif command == "delete":
    if len(sys.argv) < 3:
      print("Error: Task id is missing.")
      print("Usage: python -m main.py delete \"task_id\"")
      return
    
    try:
      task_id = int(sys.argv[2])
    except ValueError:
      print("Error: Task id must be a number.")
      return
    
    success = delete_task(task_id)
    if success:
      print(f"Task delete with task ID: {task_id}")
    else:
      print(f"No task found with ID: {task_id}")
  else:
    print(f"Unknown command: {command}")
    print("Available commands: add, list")
    
  
    
if __name__ == "__main__":
  main()