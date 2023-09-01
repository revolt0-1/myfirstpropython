# from  function import get_todo, write_todos
import function
import time


now = time.strftime("%b %d , %Y %H:%M:%S")
print("IT is" , now)
while True:
    user_action = input("Type add, show, edit , complete or exit: ")
    user_action = user_action.strip()

    if  user_action.startswith("add") :
        todo = user_action[4:]
        print(todo)

        todos = function.get_todo()

        todos.append(todo + '\n')

        function.write_todos()


    elif user_action.startswith('show'):
        # file = open('todos.txt'  ,'r')
        # todos = file.readlines()
        # file.close()

        todos = function.get_todo()

        # list_Comprehention
        # new_todos = [items.strip('\n') for items in todos]
        for index, items in enumerate(todos):
            items = items.strip('\n')
            row = f"{index  + 1} - {items} "
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number -1

            todos = function.get_todo()

            new_todo = input("Enter new todo:")
            todos[number] = new_todo + '\n'

            function.write_todos()

        except ValueError:

            print("Your command is not valid.")
            continue

            user_action = input("Type add, show, edit , complete or exit: ")
            user_action = user_action.strip()


    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = function.get_todo()

            index = number - 1
            # doubt
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            function.write_todos()

            message = f"Todo {todo_to_remove} was removed."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue



    elif 'exit' in user_action:
        break

    else :
        print("Put valid input")

print("Bye!!")

