import json

jsonlst = []
try:
    with open('./test/test.json','r') as fobj:
        jsonlst = json.load(fobj)
    print(jsonlst)
except:
    jsonlst = []


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
print(f'{jsonlst} after what i see')
jsonlst.append(dict)
with open("./test/test.json",'w') as fobj:  
    json.dump(jsonlst,fobj,indent=2)

with open("./test/test.json",'r') as fobj:
    jsonlst = json.load(fobj)

formatteddata = json.dumps(jsonlst,indent=2)
print('\n')
print(formatteddata)

target = input("Enter the username you want to update: ")
flagFound = True
for i in jsonlst:
    if i['name'] == target:
        flagFound = True
    else:
        flagFound = False
    
if flagFound:
    changeName = input("Enter the new updated username: ")
    for i in jsonlst:
        try:
            if i['name'] == target:
                i['name'] = changeName
                print('done')
            with open('./test/test.json','w') as fobj:  
                json.dump(jsonlst,fobj,indent=2)
        except:
            print('error')
else:
    print('not found')
