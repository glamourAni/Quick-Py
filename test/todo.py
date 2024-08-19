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

def get_last_id():
    content = read_file()
    arr = content['todos']
    if arr == []:
        return 0
    last_id = arr[len(arr)-1]['id']
    return last_id

def createTodo():
    """
    Create a new task
    """
    todoDict = read_file()
    
    _id = get_last_id()
    status = "pending"

    while True:
        title = input("Add a new Task/ToDo(or press q to quit): ")
        if title == "q":
            break
        else:
            _id += 1
            todo = {'description': title, 'id': _id, 'status': status}
            todoDict['todos'].append(todo)
            print("--------------------------")
            print("Task successfully created!")
            print("--------------------------")
    
    with open("todo.json", "w") as f:
        json.dump(todoDict, f, indent=2)

#createTodo()
def viewTodoList():
    """
    Read the description of a task
    """
    content = read_file()
    todos = content['todos']

    if todos == []:
        print("\nNo task added yet.")
    else:
        for todo in todos:
            print(f"\n[{todo['id']}] \"{todo['description']}\"")

def removeTodo(num):
    """
    Delete a task using its ID
    """
    content = read_file()
    todos = content['todos']
    if todos == []:
        print("\nNo task added yet.")
    else:
           for todo in todos:
            if num == todo['id']:
                t = todos.index(todo) + 1
                while(t < len(todos)):
                    todos[t]['id'] -= 1
                    t += 1
                description = todo['description']
                todos.remove(todo)
                break
    print(f"Successfully deleted task \"{description}\"")
    
    with open("todo.json", "w") as f:
        json.dump(content, f, indent=2)

def updateTodo():
    """
    Update a task using its ID
    """
    pass

def clearTasks():
    os.remove("todo.json")
    print("-------------------------------")
    print("Cleared all tasks successfully!")
    print("-------------------------------")

if __name__ == '__main__':
    Fire({
        'create': createTodo,
        'delete': removeTodo,
        'read': viewTodoList,
        'update': updateTodo,
        'clear': clearTasks
        })




