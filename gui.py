import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in your to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("add")

window = sg.Window('My To-Do App', layout=[[label],[input_box,add_button]])
# a layout expects lists , every square brac goes to next line
window.read()#displays window on screen
window.close()