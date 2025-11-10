# from functions import get_todos, write_todos
#or

import functions

while True:
    user_action=input("Type add, show, edit, complete, exit:")
    user_action=user_action.strip()

    if user_action.startswith("add"):
        todo= user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos('todos.txt',todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        new_todos = []

        for item in todos:
            new_item = item.strip("\n")
            new_todos.append(new_item)

        for index, item in enumerate(new_todos):
            print(f"{index+1}-{item}")
    elif user_action.startswith("edit") :
        try:
            number = int(user_action[5:])
            print(f"Currently {number} is {todos[number - 1]}")
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo:")
            todos[number] = new_todo + "\n"

            print("Todo", number, "changed to", new_todo)

            functions.write_todos('todos.txt',todos)
        except ValueError:
            print("Your command is invalid")
            continue

    elif user_action.startswith("complete"):
        try:
            number=int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")

            todos.pop(index)

            functions.write_todos(todos)

            message = f"{todo_to_remove} was removed from the to-do list!"
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
         
    elif user_action.startswith("exit"):
        break

    else:
        print("Command not valid.")
print("Bye!")


