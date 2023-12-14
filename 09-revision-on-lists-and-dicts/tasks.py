"""
You are hired to create an application for 
personal task management. Tasks may be open, 
blocked, in progress, or completed. The user 
will be able to add tasks, view the tasks by 
their status, and mark them accordingly.
What data structure will you use?
"""

# We are going to use a dictionary for all tasks
# with the ID of a task as the Key
# and each task will be a dictionary of the form:
# {'id': 1, 'descr': 'Do something', 'status': 'open'}
# We will use a counter 'next' to keep the ID for a new task

tasks = {}
tasks[1] = {'id': 1, 'descr': 'Buy new car', 'status': 'open'}
tasks[2] = {'id': 2, 'descr': 'Reply to manager', 'status': 'open'}
tasks[3] = {'id': 3, 'descr': 'Get invoice from client', 'status': 'blocked'}
tasks[4] = {'id': 4, 'descr': 'Paint the wall', 'status': 'in progress'}
tasks[5] = {'id': 5, 'descr': 'Replace battery', 'status': 'closed'}
next = 6

def display_menu():
    print("1. Add Task")
    print("2. View tasks (open)")
    print("3. View tasks (blocked)")
    print("4. View tasks (in progress)")
    print("5. View tasks (closed)")
    print("6. Set task status")
    print("0. EXIT")

def add_task(tasks, id):
    descr = input("Give description: ")
    task = {'id': id, 'descr': descr, 'status': 'open'}
    tasks[id] = task
    id += 1
    return tasks, id

def display_by_status(tasks, status):
    for id, task in tasks.items():
        if task['status'] == status:
            print(task)


def set_task_status(tasks):
    statuses = ['', 'open', 'blocked', 'in progress', 'closed']
    id = int(input("Give task id: "))
    if id in tasks:
        s = int(input("New status (1.Open,2.Blocked,3.InProgress,4.Closed): "))
        tasks[id]['status'] = statuses[s]
    else:
        print("Task not found")
    return tasks

while True:
    display_menu()
    choice = input("Choose: ")

    if choice == '1':
        tasks, next = add_task(tasks, next)
        print(tasks)
    elif choice == '2':
        display_by_status(tasks, 'open')
    elif choice == '3':
        display_by_status(tasks, 'blocked')
    elif choice == '4':
        display_by_status(tasks, 'in progress')
    elif choice == '5':
        display_by_status(tasks, 'closed')
    elif choice == '6':
        tasks = set_task_status(tasks)
    elif choice == '0':
        break
    else:
        print("Invalid choice")