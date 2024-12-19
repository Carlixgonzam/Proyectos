import json
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __repr__(self):
        return f"Task({self.title}, {self.description}, {self.due_date}, {self.completed})"

class TaskOrganizer:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def get_tasks(self):
        return self.tasks

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_tasks(self, filename):
        with open(filename, 'r') as file:
            tasks = json.load(file)
            self.tasks = [Task(**task) for task in tasks]

if __name__ == "__main__":
    organizer = TaskOrganizer()
    organizer.add_task("Buy groceries", "Milk, Bread, Cheese", "2023-10-15")
    organizer.add_task("Finish project", "Complete the task organizer project", "2023-10-20")
    
    print("Current tasks:")
    for task in organizer.get_tasks():
        print(task)

    organizer.save_tasks("tasks.json")
    print("Tasks saved to tasks.json")