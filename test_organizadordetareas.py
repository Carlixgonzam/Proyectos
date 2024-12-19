tasks = []


def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")


def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")


def list_tasks():
    if tasks:
        print("Tasks:")
        for task in tasks:
            print(f"- {task}")
    else:
        print("No tasks available.")


def main():
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter task to remove: ")
            remove_task(task)
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
