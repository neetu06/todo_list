
# **** Main menu ******
#
# 1. Add a new task
# 2.view all task
# 3. Remove a  task
# 4. Mark a task as completed
# 5. Exist
#
# Enter your choice:  jkl
#
# Invalid choice
#   CONCEPT USED IN THIS TO_DO PROJECT => LIST, DICTIONARY, LOOPS, FUNCTIONS AND EXCEPTION HANDLING OR ERROR HANDLING

# Step:1 Create an empty list to store the task and their status

todo_list= []


# Step 3: Define the Function to Add a New Task

def add_task():
    task = input("Enter a task: ")
    todo_list.append({"Task": task, "Status": "pending"})
    print("New  task added Successfully!")

#Step 4: Function to view All task

def view_task():
    print("Your Todo List: ")
    if len(todo_list) == 0:
         print("No pending tasks!")
    else:
         for index, task in enumerate(todo_list, 1):
             print(f"{index}. {task['Task']} - {task['Status' ]}")
    print("\n\n")

# Step:5 Function  to remove the task
def remove_task():
    if len(todo_list) == 0:
        print("List is empty!")
    else:
        try:
               search_index = int((input("Enter a task that you want to remove: ")) )- 1
               if 0 <= search_index < len(todo_list):
                  removed_task = todo_list.pop(search_index)
                  print(f"Removed task:  {removed_task["Task"]}")
               else:
                  print("Invalid task number! Try again")
        except ValueError:
                      print("Please Enter a valid number")

# Step:6 Define the function to mark a task as Done
def mark_done():
        if len(todo_list) == 0:
            print("List is empty!")
        else:
            try:
                search_index = int((input("Enter a task that you want to mark as complete: "))) - 1
                if 0 <= search_index < len(todo_list):
                     todo_list[search_index]["Status"] = "done"
                     print(f"Task {todo_list[search_index]['Task']} has been marked as done")
                else:
                    print("Invalid task number! Try again")
            except ValueError:
                print("Please Enter a valid number")


# Function to display a menu

def menu():
    while (True):
        print("Welcome to the calculator main menu")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Exit")

        choice= input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Exiting the application")
            exit()
        else:
         print("Invalid choice! Try again")

menu()





















