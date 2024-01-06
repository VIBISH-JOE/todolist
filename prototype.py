import json 

data_holder = []
def saveTodo():
    while True:    
        todo = input("What would you like to do? ")
        if todo == "quit":
            break
        else:
            data_master = {"todo": todo, "done": False}
            data_holder.append(data_master)  

    with open("data.json", "a") as fobj:
        for data in data_holder:
            json.dump(data, fobj)
            fobj.write('\n')

def show():
    with open("data.json", "r") as fobj:
        json_data = [json.loads(line) for line in fobj]
        print(json_data)

saveTodo()
show()
