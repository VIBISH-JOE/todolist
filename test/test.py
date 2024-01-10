import json

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
lst.append(dict)
with open("test.json",'w') as fobj:  
    json.dump(lst,fobj,indent=2)

with open("test.json",'r') as fobj:
    data = json.load(fobj)

formatteddata = json.dumps(data,indent=2)
print('\n')
print(formatteddata)

changeMajor = input("Do you want to change major? (y/n): ")
if changeMajor == 'y':
    major = False
    for i in data:
        i['major'] = major
    with open("test.json",'w') as fobj:  
        json.dump(data,fobj,indent=2)
    with open("test.json",'r') as fobj:
        data = json.load(fobj)
    formatteddata = json.dumps(data,indent=2)
    print('\n')
    print(formatteddata)
else:
    print('alr')