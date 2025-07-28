# -*- coding: utf-8 -*-
import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("🟡 No tasks available.")
    else:
        print("\n📝 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== 📋 To-Do List Menu ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            show_tasks(tasks)

        elif choice == '2':
            new_task = input("Enter new task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print("✅ Task added.")
            else:
                print("⚠️ Task cannot be empty.")

        elif choice == '3':
            show_tasks(tasks)
            try:
                idx = int(input("Enter task number to mark as complete: ")) - 1
                if 0 <= idx < len(tasks):
                    if "✅" not in tasks[idx]:
                        tasks[idx] += " ✅"
                        save_tasks(tasks)
                        print("✔️ Task marked as complete.")
                    else:
                        print("ℹ️ Task already marked as complete.")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == '4':
            show_tasks(tasks)
            try:
                idx = int(input("Enter task number to delete: ")) - 1
                if 0 <= idx < len(tasks):
                    removed = tasks.pop(idx)
                    save_tasks(tasks)
                    print(f"🗑️ Task '{removed}' deleted.")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == '5':
            print("👋 Goodbye! Your tasks are saved.")
            break

        else:
            print("❌ Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
