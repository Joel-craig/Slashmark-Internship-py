class ToDoList:
    """
    A class representing a simple To-Do List application.
    """

    def __init__(self):
        """
        Initializes an empty list to store tasks.
        """
        self.tasks = []

    def display_tasks(self):
        """
        Displays the tasks in the To-Do List along with their completion status.
        """
        print("Your To-Do List:")
        if not self.tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task['name']} - {'Completed' if task['completed'] else 'Not Completed'}")

    def add_task(self):
        """
        Adds a new task to the To-Do List.
        """
        task_name = input("Enter the task name: ")
        self.tasks.append({'name': task_name, 'completed': False})
        print(f"Task '{task_name}' added to the to-do list.")

    def mark_completed(self):
        """
        Marks a task in the To-Do List as completed.
        """
        self.display_tasks()
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            print(f"Task '{self.tasks[task_number - 1]['name']}' marked as completed.")
        else:
            print("Invalid task number.")

    def remove_task(self):
        """
        Removes a task from the To-Do List.
        """
        self.display_tasks()
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['name']}' has been removed from the to-do list.")
        else:
            print("Invalid task number.")

def main():
    """
    Main function to run the To-Do List application.
    """
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application:")
        print("1. Display To-Do List")
        print("2. Add a Task")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            todo_list.add_task()
        elif choice == '3':
            todo_list.mark_completed()
        elif choice == '4':
            todo_list.remove_task()
        elif choice == '5':
            print("Exiting the application. Thanks and Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
