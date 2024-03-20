tasks = []

def addtask():
    task = input("Please enter the task to be added: ")
    
    tasks.append(task)
    print(f"Task '{task}' added to the list")
def listtask():
    if not tasks:
        print("Currently no Tasks")
    else:
        print("Current Tasks: ")
        for i,task in enumerate(tasks):
            print(f"#{i}. {task}")
    

def deletetask():
    listtask()
    taskToDelete = int(input("Enter the # to delete:") )
    try:
        if taskToDelete > 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task '{taskToDelete}' is removed.")
        else:
            print("Not Found")
    except:
        print("Invalid Input")


if __name__ == "__main__":
    print("To Do List")
    while True:
        print("\nSelect any one of the options")
        print("-----------------------------")
        print("1: Add")
        print("2: Delete")
        print("3: List")
        print("4: Quit")

        choice = input("Enter your choice: ")
        if (choice == "1"):
            addtask()
        elif (choice == "2"):
            deletetask()

        elif (choice == "3"):
            listtask()

        elif (choice == "4"):
            break

        else:
            print("Invalid Input")
    print("Good Bye ")