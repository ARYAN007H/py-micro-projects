import datetime

def display_menu():
    print("To-Do List App")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Quit")

def add_task(tasks):
    task_name = input("Enter task name: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    try:
        due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    tasks.append({"name": task_name, "due_date": due_date, "completed": False})
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks added yet.")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "Incomplete" if not task["completed"] else "Completed"
            print(f"{i}. {task['name']} (Due: {task['due_date'].strftime('%Y-%m-%d')}) - {status}")

def mark_task_as_completed(tasks):
    if not tasks:
        print("No tasks added yet.")
    else:
        task_index = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_index <= len(tasks):
            tasks[task_index - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

def delete_task(tasks):
    if not tasks:
        print("No tasks added yet.")
    else:
        task_index = int(input("Enter the task number to delete: "))
        if 1 <= task_index <= len(tasks):
            del tasks[task_index - 1]
            print("Task deleted.")
        else:
            print("Invalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            mark_task_as_completed(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
