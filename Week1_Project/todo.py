# Decode Labs Week 1 To-Do List

tasks = []
task_id = 1

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Add task
    if choice == "1":
        task_name = input("Enter task: ")

        task = {
            "id": task_id,
            "task_name": task_name
        }

        tasks.append(task)
        task_id += 1

        print("Task added successfully!")

    # View tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available")

        else:
            print("\nYour Tasks:")
            for task in tasks:
                print(
                    f"ID: {task['id']} | Task: {task['task_name']}"
                )

    # Exit
    elif choice == "3":
        print("Program closed")
        break

    else:
        print("Invalid choice")