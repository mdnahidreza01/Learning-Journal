# ToDO List:

def todo_app():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. View  2. Add  3. Delete  4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            if not tasks:
                print("Your list is empty.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "2":
            task = input("Enter new task: ")
            tasks.append(task)
            print(f"Added: '{task}'")

        elif choice == "3":
            if not tasks:
                print("No tasks to delete.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                num = int(input("Enter task number to delete: "))
                removed = tasks.pop(num - 1)
                print(f"Deleted: '{removed}'")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    todo_app()
