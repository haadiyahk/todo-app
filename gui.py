import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in your to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box,add_button]],
                   font=('Helvetica',20))
# a layout expects lists , every square brac goes to next line
# each row in the gui layout has to be a list

while True:
    event, values = window.read() #Add{'key of i/p box': 'whatever was entered in the i/p box'}
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case sg.WIN_CLOSED:
            #sg is the imported module - FreeSimpleGUI
            #WIN_CLOSED is a var defined in freesimplegui. this closes the program correctly when we click on the "x". exit button
            break

window.close()

