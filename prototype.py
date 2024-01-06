import json
data_holder = []
while True:    
    todo = input("What would you like to do? ")
    if todo == "quit":
        break
    else:
        data_master = {"todo": todo,"done": False}
    with open("data.json", "a") as fobj:
        json.dump(data_master, fobj)

with open("data.json", "r") as fobj:
    json_data = json.load(fobj)
    print(json_data)