import json

data_holder = []

def read():
    global data_holder
    try:
        with open('data.json','r') as fobj:
            data_holder = json.load(fobj)
            print('read')
            print(data_holder)
    except:
        data_holder = []
        print('init')

def write():
    while True:
        todo = input("Enter the Todo: ")
        if todo == "quit":
            break
        else:
            data = {
                'todo': todo,
                'done': False
            }
            print(data_holder)
            data_holder.append(data)
        with open('data.json','w') as fobj:
            json.dump(data_holder,fobj,indent=2)

read()
write()