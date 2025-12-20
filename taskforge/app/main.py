import sys
# from app.db import init_db, add_task, list_tasks, update_status, delete_task
from app.db import *

def print_tasks(tasks):
  print("Tasks: ")
  for index, (task_id, desc, status, created_at) in enumerate(tasks, start=1):
    print(f"{index}. {desc}")
    print(f"   status      : {status}")
    print(f"   Created At  : {created_at}")
    print(f"   (id: {task_id})")
    print("-" * 40)

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
    if len(sys.argv) == 2:
      tasks =list_tasks()
    else:
      status = sys.argv[2]
      if status not in ("pending", "completed"):
        print("Error: status must be 'pending' or 'completed'")
        return
      
      tasks = get_tasks_by_status(status)
    
    print_tasks(tasks)
    
  elif command == "update":
    if len(sys.argv) < 3:
      print("Error: Task id is missing.")
      print("Usage: python -m main.py update <index>")
      return
    
    try:
      index = int(sys.argv[2])
    except ValueError:
      print("Error: Index must be a number.")
      return

    tasks = list_tasks()
    
  
    if index < 1 or index > len(tasks):
      print(f"Error: Index must be between 1 and {len(tasks)}")
      return
    
    task_id = tasks[index - 1][0]
    
    success = update_status(task_id)
    
    if success:
      print(f"status updated for task ID: {task_id}")
    else:
      print(f"No task found with ID: {task_id}")
  
  elif command == "delete":
    if len(sys.argv) < 3:
      print("Error: Task id is missing.")
      print("Usage: python -m main.py delete <index>")
      return
    
    try:
      index = int(sys.argv[2])
    except ValueError:
      print("Error: Index must be a number.")
      return
    
    
    tasks = list_tasks()
    
    if index < 1 or index > len(tasks):
      print(f"Error: Invalid index. Choose between 1 and {len(tasks)}.")
      return
    
    task_id = tasks[index - 1][0]
    success = delete_task(task_id)
    
    if success:
      print(f"Task deleted successfully (ID: {task_id})")
    else:
      print(f"No task found with ID: {task_id}")


  else:
    print(f"Unknown command: {command}")
    print("Available commands: add, list")
    
  
    
if __name__ == "__main__":
  main()