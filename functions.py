import json

data_holder = []

def read():
    global data_holder
    try:
        with open('data.json','r') as fobj:
            data_holder = json.load(fobj)
    except:
        data_holder = []

def write(todo):
    data = {
        'todo': todo,
        'done': False
    }
    data_holder.append(data)
    with open('data.json','w') as fobj:
        json.dump(data_holder,fobj,indent=2)
    print("done")
        

def marktodo(mktodo):
    read()
    flagFound = False
    for i in data_holder:
        if i['todo'] == mktodo:
            flagFound = True
            break
    if flagFound:
            try:
                i['done'] = True
                with open('data.json','w') as fobj:
                    json.dump(data_holder,fobj,indent=2)
                return 'done'
            except:
                return 'error'
            
    else:
        return 'element not found'

def delTodo(deltodo):
    read()
    flagFound = False
    for i in data_holder:
        if i['todo'] == deltodo:
            flagFound = True
            break
    if flagFound:
        data_holder.remove(i)
        with open('data.json','w') as fobj:
            json.dump(data_holder,fobj,indent=2)
        return 'done'
    else:
        return 'element not found'
