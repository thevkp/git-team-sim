import sys
from app.db import init_db, add_task, list_tasks


def main():
  init_db()
  
  if len(sys.argv) < 3:
    print("Usage: python main.py add \"task description\"")
    return 
  
  command = sys.argv[1]
  
  if command == "add":
    description = " ".join(sys.argv[2:])
    add_task(description)
    print("Task added succesfully")
    
  elif command == "list":
    tasks = list_tasks()
    if not tasks:
      print("No tasks found")
    else:
      for task_id, desc in tasks:
        print(f"{task_id}. {desc}")
    
    
if __name__ == "__main__":
  main()