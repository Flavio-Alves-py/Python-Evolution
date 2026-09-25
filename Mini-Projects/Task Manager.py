class TaskManager:
    def __init__(self):
        self.task = {}
        self.task_id = [x for x in range(1, 11)]
        self.tasklst = []

    def show_tasks(self):
        for k,v in self.task.items():
            print(f"{k}: {v}")

    def add_task(self):
        task = input("Enter a task: ")
        self.tasklst.append(task)
        for i in range(len(self.tasklst)):
            self.task[self.task_id[i]] = self.tasklst[i]
        print(f"Task '{task}' added.")

if __name__ == "__main__":
    task_manager = TaskManager()
    while True:
        print("\nTask Manager")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task_manager.show_tasks()
        elif choice == '2':
            task_manager.add_task()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")