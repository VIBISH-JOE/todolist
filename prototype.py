import json

data_holder = []

def saveJson():
    while True:
        todo = input("Enter the todo list (type 'quit' to exit): ")
        if todo.lower() == 'quit':
            break
        else:
            data = {
                "todo": todo
            }
            data_holder.append(data)
            with open("data.json", 'w') as jfobj:
                json.dump(data_holder, jfobj)

def showJson():
    try:
        with open('data.json', 'r') as fobj:
            data = json.load(fobj)
            print(data)
    except FileNotFoundError:

        print("No data found.")
        
# Main
saveJson()
showJson()
