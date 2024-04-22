def display_menu():
    print("\nTo-Do List Program")
    print("1. View To-Do List")
    print("2. Add task to list")
    print("3. Delete Task from list")
    print("4. Exit")
    choice = input("Enter Choice: ")
    return choice

def view_tasks(task_list):
    if not task_list:
        print("Your to-do list is empty")

    else:
        print("\nTo-Do list:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

def add_task(task_list):
    task = input("Enter a task to add: ")
    task_list.append(task)
    print(f"'{task}' has been added to the list.")

def delete_task(task_list):
    view_tasks(task_list)
    if task_list:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(task_list):
            removed_task = task_list.pop(task_num-1)
            print(f"'{removed_task}' has been removed from list.")
        else:
            print("Invalid task number")

def main():
        task_list = []

        while True:
            user_choice = display_menu()

            if user_choice == "1":
                view_tasks(task_list)
            elif user_choice == "2":
                add_task(task_list)
            elif user_choice == "3":
                delete_task(task_list)
            elif user_choice == "4":
                print("exiting Program")
                break
            else:
                print("Invalid choice. please select a valid options")


if __name__ == "__main__":
    main()