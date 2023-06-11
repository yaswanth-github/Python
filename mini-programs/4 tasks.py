class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added task '{task}' to the to-do list.")
    
    def complete_task(self, task_index):
        try:
            task = self.tasks[task_index]
        except IndexError:
            print("Invalid task index! Please enter a valid index.")
            return
        
        self.tasks[task_index] = f"[X] {task}"
        print(f"Completed task '{task}'.")
    
    def view_list(self):
        if not self.tasks:
            print("The to-do list is empty!")
        else:
            print("To-do list:")
            for task in self.tasks:
                print(f"- {task}")
    
    def clear_list(self):
        self.tasks = []
        print("The to-do list has been cleared.")

def create_task(todo_list):
    task = input("Enter a new task: ")
    todo_list.add_task(task)

def mark_task_complete(todo_list):
    task_index = input("Enter the index of the task to mark as complete: ")
    try:
        task_index = int(task_index)
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    todo_list.complete_task(task_index)

def display_list(todo_list):
    todo_list.view_list()

def clear_all(todo_list):
    confirm = input("Are you sure you want to clear the entire to-do list? (y/n) ")
    if confirm == "y":
        todo_list.clear_list()

def main():
    todo_list = TodoList()
    
    while True:
        print("Menu:")
        print("1. Create a task")
        print("2. Mark a task as complete")
        print("3. View the to-do list")
        print("4. Clear the entire to-do list")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_task(todo_list)
        elif choice == "2":
            mark_task_complete(todo_list)
        elif choice == "3":
            display_list(todo_list)
        elif choice == "4":
            clear_all(todo_list)
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please enter a valid choice.")
    
    print("Goodbye!")

if __name__ == "__main__":
    main()
