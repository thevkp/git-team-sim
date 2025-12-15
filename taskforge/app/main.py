import sys
from app.db import init_db, add_task


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
    
    
if __name__ == "__main__":
  main()