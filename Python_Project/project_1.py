# import os

# # Create a file to store the to-do list items
# if not os.path.exists("todo.txt"):
#     with open("todo.txt", "w") as file:
#         pass

# def add_item():
#     # Get the item from the user
#     item = input("Enter the item: ")
    
#     # Add the item to the file
#     with open("todo.txt", "a") as file:
#         file.write(item + "\n")
    
#     print("Item added successfully.")
    
# def read_items():
#     # Read the items from the file
#     with open("todo.txt", "r") as file:
#         items = file.readlines()
        
#     if not items:
#         print("No items found.")
#     else:
#         # Display the items to the user
#         for i, item in enumerate(items, start=1):
#             print(f"{i}. {item.strip()}")

# def update_item():
#     # Get the item number from the user
#     item_num = int(input("Enter the item number to update: "))
    
#     # Get the new item from the user
#     new_item = input("Enter the new item: ")
    
#     # Update the item in the file
#     with open("todo.txt", "r") as file:
#         items = file.readlines()
    
#     if item_num <= 0 or item_num > len(items):
#         print("Invalid item number.")
#     else:
#         items[item_num-1] = new_item + "\n"
#         with open("todo.txt", "w") as file:
#             file.writelines(items)
#         print("Item updated successfully.")

# def delete_item():
#     # Get the item number from the user
#     item_num = int(input("Enter the item number to delete: "))
    
#     # Delete the item from the file
#     with open("todo.txt", "r") as file:
#         items = file.readlines()
    
#     if item_num <= 0 or item_num > len(items):
#         print("Invalid item number.")
#     else:
#         del items[item_num-1]
#         with open("todo.txt", "w") as file:
#             file.writelines(items)
#         print("Item deleted successfully.")

# # Main loop
# while True:
#     print("\n1. Add Item")
#     print("2. Read Items")
#     print("3. Update Item")
#     print("4. Delete Item")
#     print("5. Exit")
    
#     choice = int(input("Enter your choice: "))
    
#     if choice == 1:
#         add_item()
#     elif choice == 2:
#         read_items()
#     elif choice == 3:
#         update_item()
#     elif choice == 4:
#         delete_item()
#     elif choice == 5:
#         break
#     else:
#         print("Invalid choice.")

#initializing an empty list
list = []

while True:
    # Display menu
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    #for add task
    if choice == "1":
        task = input("Enter the task: ")
        list.append(task)
        print("Task added successfully.")
    #for view task
    elif choice == "2":
        if not list:
            print("No tasks found.")
        else:
            print("------------------------------------------------------\n")
            print("Tasks:")
            for i, task in enumerate(list, start=1):
                print(f"{i}. {task}")
            print("------------------------------------------------------\n")
    #for Mark as done
    elif choice == "3":
        if not list:
            print("No tasks found.")
        else:
            print("------------------------------------------------------\n")
            task_num = int(input("Enter the task number to mark as done: "))
            if task_num <= 0 or task_num > len(list):
                print("Invalid task number.")
                print("------------------------------------------------------\n")
            else:
                del list[task_num-1]
                print("Task marked as done.")
            print("------------------------------------------------------\n")
    #for exit
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
