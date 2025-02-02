from datetime import datetime
import json
import os

class Task:
    """
    A class to represent an individual task.
    
    Attributes:
        description (str): The task description
        priority (str): Priority level of the task (High/Medium/Low)
        due_date (str): Due date of the task
        category (str): Category of the task
        completed (bool): Completion status of the task
    """
    
    def __init__(self, description, priority="Medium", due_date=None, category="General"):
        """Initialize a new task with given attributes."""
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.category = category
        self.completed = False
    
    def to_dict(self):
        """Convert task to dictionary for JSON serialization."""
        return {
            "description": self.description,
            "priority": self.priority,
            "due_date": self.due_date,
            "category": self.category,
            "completed": self.completed
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a Task instance from dictionary data."""
        task = cls(data["description"])
        task.priority = data["priority"]
        task.due_date = data["due_date"]
        task.category = data["category"]
        task.completed = data["completed"]
        return task

class TodoList:
    """
    A class to represent a Todo List application.
    
    This class provides functionality to manage tasks including adding,
    viewing, and removing tasks from a todo list.
    
    Attributes:
        tasks (list): A list to store all todo tasks
    """
    
    def __init__(self):
        """Initialize an empty TodoList with no tasks."""
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()

    def add_task(self):
        """Add a new task with all attributes."""
        description = input("Enter task description: ")
        
        print("\nPriority Levels:")
        print("1. High")
        print("2. Medium")
        print("3. Low")
        priority_choice = input("Choose priority (1-3) [2]: ").strip() or "2"
        priority_map = {"1": "High", "2": "Medium", "3": "Low"}
        priority = priority_map.get(priority_choice, "Medium")
        
        due_date = input("Enter due date (YYYY-MM-DD) [optional]: ").strip()
        if due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Due date set to None.")
                due_date = None
        
        category = input("Enter category [General]: ").strip() or "General"
        
        task = Task(description, priority, due_date, category)
        self.tasks.append(task)
        print(f"Task '{description}' added successfully!")
        self.save_tasks()

    def view_tasks(self, show_completed=True):
        """
        Display all tasks in the todo list.
        
        Args:
            show_completed (bool): Whether to show completed tasks
        """
        if not self.tasks:
            print("No tasks in your to-do list!")
            return
        
        print("\nYour To-Do List:")
        for index, task in enumerate(self.tasks, 1):
            if not show_completed and task.completed:
                continue
            
            status = "✓" if task.completed else " "
            due_str = f", Due: {task.due_date}" if task.due_date else ""
            print(f"{index}. [{status}] {task.description} "
                  f"(Priority: {task.priority}, Category: {task.category}{due_str})")

    def remove_task(self, index):
        """Remove a task from the todo list by its index."""
        if 1 <= index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            print(f"Task '{removed_task.description}' removed successfully!")
            self.save_tasks()
        else:
            print("Invalid task number!")

    def toggle_task_completion(self, index):
        """Toggle the completion status of a task."""
        if 1 <= index <= len(self.tasks):
            task = self.tasks[index - 1]
            task.completed = not task.completed
            status = "completed" if task.completed else "uncompleted"
            print(f"Task '{task.description}' marked as {status}!")
            self.save_tasks()
        else:
            print("Invalid task number!")

    def save_tasks(self):
        """Save tasks to a JSON file."""
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=2)

    def load_tasks(self):
        """Load tasks from JSON file if it exists."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                try:
                    tasks_data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in tasks_data]
                except json.JSONDecodeError:
                    self.tasks = []

def main():
    """
    Main function to run the Todo List application.
    
    Provides a command-line interface with a menu of options:
    1. Add Task: Allows user to add a new task
    2. View All Tasks: Displays all current tasks
    3. View Active Tasks: Displays only active tasks
    4. Remove Task: Allows user to remove a task by its number
    5. Toggle Task Completion: Allows user to toggle the completion status of a task
    6. Exit: Terminates the application
    
    The function runs in a loop until the user chooses to exit.
    """
    todo = TodoList()
    
    while True:
        print("\n=== To-Do List Application ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Active Tasks")
        print("4. Remove Task")
        print("5. Toggle Task Completion")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            todo.add_task()
        
        elif choice == '2':
            todo.view_tasks(show_completed=True)
        
        elif choice == '3':
            todo.view_tasks(show_completed=False)
        
        elif choice == '4':
            todo.view_tasks()
            if todo.tasks:
                try:
                    index = int(input("Enter the task number to remove: "))
                    todo.remove_task(index)
                except ValueError:
                    print("Please enter a valid number!")
        
        elif choice == '5':
            todo.view_tasks()
            if todo.tasks:
                try:
                    index = int(input("Enter the task number to toggle completion: "))
                    todo.toggle_task_completion(index)
                except ValueError:
                    print("Please enter a valid number!")
        
        elif choice == '6':
            print("Thank you for using the To-Do List application!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main() 