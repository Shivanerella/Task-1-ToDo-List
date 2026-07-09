# List to store tasks
my_tasks = []

# Infinite loop to display the menu
while True:

    # Display menu
    print("1. Add a task")
    print("2. View tasks")
    print("3. Exit")

    # Get user's choice
    choice = input("Enter your choice: ")

    # Add a new task
    if choice == "1":
        task = input("Enter the task: ")
        my_tasks.append(task)
        print("Task Added Successfully!\n")

    # View all tasks
    elif choice == "2":
        if len(my_tasks) == 0:
            print("No tasks available.\n")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(my_tasks, start=1):
                print(f"{i}. {task}")
            print()

    # Exit the program
    elif choice == "3":
        print("Exiting the program.")
        break

    # Handle invalid choice
    else:
        print("Invalid Choice! Please try again.\n")