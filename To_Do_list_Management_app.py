#lets start making to do list using pyhton
FILE_NAME = "tasks.txt"

def load_task():
    tasks = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                task, status = line.strip().split("|")
                tasks.append({"task": task, "done": status == "1"})
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for t in tasks:
            status = "1" if t["done"] else "0"
            file.write(f"{t['task']}|{status}\n")


def view_task(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for i, t in enumerate(tasks, start=1):
        status = "✔" if t["done"] else "✖"
        print(f"{i}. {t['task']} [{status}]")


def create_task(tasks):
    task_name = input("Enter task name: ")
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print("Task added successfully.")


def mark_task_complete(tasks):
    view_task(tasks)
    num = int(input("Enter task number to mark complete: "))

    if 1 <= num <= len(tasks):
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")


def main():
    tasks = load_task()

    while True:
        print("\n------------------------")
        print("  To-Do List Manager")
        print("------------------------")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_task(tasks)
        elif choice == 2:
            create_task(tasks)
        elif choice == 3:
            mark_task_complete(tasks)
        elif choice == 4:
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.")


main()
#done with project lets start making
# and good luck                   

