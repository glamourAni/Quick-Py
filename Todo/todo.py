from fire import Fire
import os
import json

def read_file():
    try:
        with open("todo.json") as f:
            content = json.load(f)
            return content
    except:
        return {'todos': []}

def save_file(content):
    with open("todo.json","w") as f:
        json.dump(content, f, indent=2)

def get_last_id():
    content = read_file()
    arr = content['todos']
    if not len(arr):
        return 0
    last_id = arr[len(arr)-1]['id']
    return last_id

def createTodo():
    """
    Create a new task. | Usage: create
    """
    todoDict = read_file()
    
    _id = get_last_id()
    status = "pending"

    while True:
        title = input("Add a new Task/ToDo(or press q to quit): ")
        if title == "q":
            break
        elif len(title) < 3:
            print("Chracters must have a minimum length of 3\n")
        else:
            _id += 1
            todo = {'description': title, 'id': _id, 'status': status}
            todoDict['todos'].append(todo)
            print("--------------------------")
            print("Task successfully created!")
            print("--------------------------\n")
    
    save_file(todoDict)
#createTodo()
def viewTodoList():
    """
    View all tasks.[Usage: view]
    """
    content = read_file()
    todos = content['todos']

    if not len(todos):
        print("\nNo task added yet.")
    else:
        for todo in todos:
            print(f"\n[{todo['id']}] \"{todo['description']}\"\t*{todo['status']}*")

def removeTodo(num):
    """
    Delete a task using its ID.[Usage: remove ID, where ID=task_id]
    """
    content = read_file()
    todos = content['todos']
    if not len(todos):
        print("\nNo task added yet.")
    else:
        for todo in todos:
            if type(num) == int:
                if num > len(todos):
                    return "Task doesn't exist"
                if num == todo['id']:
                    t = todos.index(todo) + 1
                    while(t < len(todos)):
                        todos[t]['id'] -= 1
                        t += 1
                    description = todo['description']
                    todos.remove(todo)
                    break
                
                    #print(f"Task with ID {num} does not exist.")
            else:
                print(f"{num} is not a valid ID. ID must be a whole number.")
    print(f"Successfully deleted task \"{description}\"")
    
    save_file(content)

def updateTodo(num):
    """
    Edit a task using its ID.[Usage: update ID, where ID=task_id]
    """
    content = read_file()
    todos = content['todos']
    if not len(todos):
        print("\nNo task added yet.")
    else:
        for todo in todos:
            if type(num) == int:
                if len(todo) < num:
                    return f"Task with id:{todo['id']} does not exist"
                if num == todo['id']:
                    edit_todo = input("Add a task: ")
                    todo['description'] = edit_todo
                    print ("Task updated successfully!")

    save_file(content)
                
def clearTasks():
    """
    Clear all tasks
    Usage: clear
    """
    os.remove("todo.json")
    print("-------------------------------")
    print("Cleared all tasks successfully!")
    print("-------------------------------")

def status(num, check=False, uncheck=False):
    """
    Update the status of a task.[Usage: status ID flag, where ID=task_id and flag is one of the following 
    |--check: mark task as completed|--uncheck: mark task as pending]
    """
    content = read_file()
    todos = content['todos']

    if check:
        for todo in todos:
            if type(num) == int:
                if num == todo['id']:
                    todo['status'] = 'completed'
                    print(f"\"{todo['description']}\" marked as completed!")
            else:
                print(f"{num} is not a valid ID. ID must be a whole number.")
    if uncheck:
        for todo in todos:
            if type(num) == int:
                if num == todo['id']:
                    todo['status'] = 'pending'
                    print(f"\"{todo['description']}\" marked as pending!")
            else:
                print(f"{num} is not a valid ID. ID must be a whole number.")

    save_file(content)
        

if __name__ == '__main__':
    Fire(
         {
        'clear': clearTasks,
        'create': createTodo,
        'delete': removeTodo,
        'read': viewTodoList,
        'status': status,
        'update': updateTodo
        })
