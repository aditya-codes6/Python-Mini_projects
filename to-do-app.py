
tasks = []

while True:
    print("\n===== TO-DO APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append({"name": task, "done": False})
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found!")
        else:
            for i, task in enumerate(tasks, start=1):
                if task["done"]:
                    status = "Completed"
                else:
                    status = "Pending"

                print(i, ".", task["name"], "-", status)

    elif choice == "3":
        for i, task in enumerate(tasks, start=1):
            print(i, ".", task["name"])

        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            print("Task completed!")
        else:
            print("Invalid task number!")

    elif choice == "4":
        for i, task in enumerate(tasks, start=1):
            print(i, ".", task["name"])

        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print("Deleted:", removed["name"])
        else:
            print("Invalid task number!")

    elif choice == "5":
        print("Thank you for using the To-Do App!")
        break

    else:
        print("Invalid choice! Try again.")
