#To Do List

print("TO DO LIST")
todo_list=[] # Empty list to add tasks

def showtask():
    if not todo_list:
        print("No Existed Tasks..")
    else:
        for i, task in enumerate(todo_list, 1): # Enumerate is used in loop and it consider both task and index
            print(f"{i}. {task}")

def addtask(task):
    todo_list.append(task)
    print("Task added..")
def delete(index):
    if 0 < index <= len(todo_list):
        removed = todo_list.pop(index-1)
        print(f"Removed: {removed}")
    else:
        print("Invalid task number..")
while True:
    print("\n1. View Tasks\n2. Add Tasks\n3. Delete Tasks\n4.Exit\n") 
    a = int(input("Enter your choice: "))
    if a == 1:
        showtask()
    elif a == 2:
        task = input("Enter the task: ")
        addtask(task) 
    elif a == 3:
        showtask()
        try:
            b = int(input("Enter the task number to removed: "))
            delete(b) 
        except ValueError:
            print("Enter a valid task number..")
    elif a == 4:
        print("GoodBye!!")
        break
    else:
        print("Invalid Choice Number..")
                    

