import functions as fn

while True:
    addTodo = input("Enter the Todo that you want to add: ")
    if addTodo == "q":
        break
    else:
        fn.write(addTodo)


mktodo = input("Enter the Todo That you want to mark as done: ")
print(fn.marktodo(mktodo))

delTodo = input("Enter the Todo That you want to delete: ")
print(fn.delTodo(delTodo))