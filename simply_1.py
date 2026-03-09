import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self, filename='todos.json'):
        self.filename = filename
        self.todos = self.load_todos()
    
    def load_todos(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []
    
    def save_todos(self):
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=2)
    
    def add_task(self, task):
        todo = {
            'id': len(self.todos) + 1,
            'task': task,
            'completed': False,
            'created': datetime.now().strftime('%Y-%m-%d %H:%M')
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"✓ Added: {task}")
    
    def list_tasks(self):
        if not self.todos:
            print("No tasks yet!")
            return
        
        print("\n📋 Your Tasks:")
        print("-" * 50)
        for todo in self.todos:
            status = "✓" if todo['completed'] else "○"
            print(f"{status} [{todo['id']}] {todo['task']}")
            print(f"   Created: {todo['created']}")
        print("-" * 50)
    
    def complete_task(self, task_id):
        for todo in self.todos:
            if todo['id'] == task_id:
                todo['completed'] = True
                self.save_todos()
                print(f"✓ Completed: {todo['task']}")
                return
        print("Task not found!")
    
    def delete_task(self, task_id):
        for i, todo in enumerate(self.todos):
            if todo['id'] == task_id:
                removed = self.todos.pop(i)
                self.save_todos()
                print(f"✓ Deleted: {removed['task']}")
                return
        print("Task not found!")
    
    def run(self):
        print("🎯 Simple To-Do List App")
        
        while True:
            print("\nCommands: [a]dd, [l]ist, [c]omplete, [d]elete, [q]uit")
            choice = input("→ ").lower().strip()
            
            if choice == 'a':
                task = input("Task: ")
                if task:
                    self.add_task(task)
            
            elif choice == 'l':
                self.list_tasks()
            
            elif choice == 'c':
                try:
                    task_id = int(input("Task ID to complete: "))
                    self.complete_task(task_id)
                except ValueError:
                    print("Invalid ID!")
            
            elif choice == 'd':
                try:
                    task_id = int(input("Task ID to delete: "))
                    self.delete_task(task_id)
                except ValueError:
                    print("Invalid ID!")
            
            elif choice == 'q':
                print("Goodbye! 👋")
                break
            
            else:
                print("Invalid command!")

if __name__ == "__main__":
    app = TodoApp()
    app.run()