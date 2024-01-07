import json

data_holder = []

try:
    with open('data.json', 'r') as fobj:
        data_holder = json.load(fobj)
        if len(data_holder) == 0:
             print("empty")
except FileNotFoundError:
    print("No data found.")

def saveJson():
    while True:
        todo = input("Enter the todo list (type 'quit' to exit): ")
        if todo.lower() == 'quit':
            print(data_holder)
            break
        else:
            data = {
                "todo": todo,
                "done": False
            }
            data_holder.append(data)
            with open("data.json", 'w') as jfobj:
                json.dump(data_holder, jfobj, indent=2)

# Main
saveJson()
