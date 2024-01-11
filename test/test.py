import json

lst = []
try:
    with open('test.json','r') as fobj:
        lst = json.load(fobj)
    print(lst)
except:
    lst = []


name = input("Enter the name: ")
user = input("Enter the username: ")
passwork = input("Enter the password: ")
are_you_major = input("Are you major? (y/n): ")
IfMajor = False
if are_you_major == 'y':
    IfMajor = True

dict = {
    "name": name,
    "user": user,
    "password": passwork,
    "major": IfMajor,
}
print(f'{lst} after what i see')
lst.append(dict)
with open("test.json",'w') as fobj:  
    json.dump(lst,fobj,indent=2)

with open("test.json",'r') as fobj:
    lst = json.load(fobj)

formatteddata = json.dumps(lst,indent=2)
print('\n')
print(formatteddata)

target = input("Enter the username you want to update: ")
flagFound = True
for i in lst:
    if i['name'] == target:
        flagFound = True
    else:
        flagFound = False
    
if flagFound:
    changeName = input("Enter the new updated username: ")
    for i in lst:
        try:
            if i['name'] == target:
                i['name'] = changeName
                print('done')
            with open("test.json",'w') as fobj:  
                json.dump(lst,fobj,indent=2)
        except:
            print('error')
else:
    print('not found')
