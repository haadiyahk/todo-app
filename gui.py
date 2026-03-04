import functions
import FreeSimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text('', key="clock")
label = sg.Text("Type in your to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45,10])
                    #enable arg expects true or false, size is how the listbox will look
edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")
window = sg.Window('My To-Do App',
                   # below in layout are all the rows
                   layout=[[clock],
                           [label],
                           [input_box,add_button],
                           [list_box,edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica',20))
# a layout expects lists , every square brac goes to next line
# each row in the gui layout has to be a list

while True:
    event, values = window.read(timeout=200)
    #python checks what the user clicked using match/case. so every case = something the user clicked in gui
    #Add{'key of i/p box': 'whatever was entered in the i/p box'}
    window["clock"].update(value=time.strftime("%b, %d, %Y, %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            # show the updates in real time

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                #get the todoitem(values) the user selected from the list('todos')
                new_todo = values['todo']
                #get the new text the user entered for this todoo

                todos = functions.get_todos()
                #load the full list of todos form the file
                index= todos.index(todo_to_edit)
                #whats the index(position) of the todoo to be edited
                todos[index]= new_todo
                #overwrite the old task with the updated one

                functions.write_todos(todos)
                #make the change permanent
                window['todos'].update(values=todos)
                #show the updates in real time
            except IndexError:
                sg.popup("please select an item to edit.", font=("Helvetica",20))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("please select an item to complate" , font=("Helvetica",20))


        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])
            #when a todoo is clicked show it in the input box so it can be edited

        case sg.WIN_CLOSED:
            #sg is the imported module - FreeSimpleGUI
            #WIN_CLOSED is a var defined in freesimplegui. this closes the program correctly when we click on the "x". exit button
            break

window.close()

