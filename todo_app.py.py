#Global Var for Empty list to store tasks
task_list = []

#Function adds tasks to task_list
def add_task(task):
    task_list.append(task)
    print("Task added successfully!")

#Function returns list values
def view_tasks():
    global task_list
    if not task_list:
        print("No tasks to display.")
    else:
        print("To-do:")
        for index, task_item in enumerate(task_list, start=1):
            print(f"{index}. {task_list}")

#Function to remove a task from the list.
def remove_task(index):
    if 1 <= index <= len(task_list):
        removed_task = task_list.pop(index - 1)
        print(f"Task '{removed_task}' removed successfully.")
    else:
        print("Nothing Removed")

#While loop, to select options
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice: ")
#Conditionals for choices
    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        index = int(input("Enter the task number to remove: "))
        remove_task(index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")