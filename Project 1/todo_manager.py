import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read tasks.json. Starting with an empty list.")
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    task_name = input("\nEnter your task: ").strip()

    if not task_name:
        print("Error: Task cannot be empty.")
        return

    next_id = max((task["id"] for task in tasks), default=0) + 1
    new_task = {
        "id": next_id,
        "task": task_name,
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!")


def view_tasks(tasks):
    print("\n========== YOUR TASKS ==========")

    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            status = "Completed" if task.get("completed", False) else "Pending"
            print(f'{task["id"]}. {task["task"]} [{status}]')

    print("================================")


def main():
    tasks = load_tasks()

    while True:
        print("\n================================")
        print("       TO-DO LIST MANAGER")
        print("================================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            print("\nThank you for using To-Do List Manager!")
            print("Your tasks have been saved.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
