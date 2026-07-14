with open("todo_list.txt", "a"):
    pass

tasks = []

with open("todo_list.txt") as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()
    tasks.append(line)

while True:
    print("\n==== TO-DO LIST ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nView Tasks")

        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ":", tasks[i])

    elif choice == 2:
        print("\nAdd Task")

        task = input("Enter your task: ")

        if task.strip() == "":
            print("Task cannot be empty!")
        else:
            tasks.append(task)

            with open("todo_list.txt", "w") as f:
                for task in tasks:
                    f.write(task)
                    f.write("\n")

            print("Task added successfully!")

    elif choice == 3:
        print("\nRemove Task")

        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ":", tasks[i])

            index = int(input("Enter the task number to remove: "))

            if index < 1 or index > len(tasks):
                print("Invalid task number!")
            else:
                removed_task = tasks.pop(index - 1)

                with open("todo_list.txt", "w") as f:
                    for task in tasks:
                        f.write(task)
                        f.write("\n")

                print(f'"{removed_task}" removed successfully!')

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")