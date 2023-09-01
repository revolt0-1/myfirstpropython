
import PySimpleGUI as sg
import function
import time

sg.theme("lightBlue1")
clock = sg.Text('',key="clock")

label = sg.Text("Type in a To-Do ")
# labels  = ("Type in  To-DO" , "FIle")
# size = max(map(len , labels))
# file_label = sg.Text("Filename")
input_box = sg.InputText(tooltip="Enter todo" ,key='todo')
# input_box1 = sg.InputText(tooltip="Enter File" ,key='file')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=function.get_todo('allinone/todos.txt'), key='todos', enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")
window = sg.Window('My To-Do app',
                   layout=[[label], [input_box, add_button], [list_box, edit_button, complete_button]],
                   font=('Helvetica', 15))
# layout = [
#     [sg.Text(label , size = size) , sg.Input( key=label.split()[0])]
#     for label in labels] + [
#     [sg.Push() , sg.Button('Send')]
#
# ]
#
while True:
    event, values = window.read()
    window['clock'].update(value = time.strftime("%b %d , %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            # todos = function.get_todo('allinone/todos1.txt')
            todos = function.get_todo('allinone/todos.txt')
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            function.write_todos(todos, 'allinone/todos.txt')
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = function.get_todo('allinone/todos.txt')
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                function.write_todos(todos, 'allinone/todos.txt')
                window['todos'].update(values=todos)

            except IndexError:
                print("Please select an item first")


            sg.popup("Please select an item first.", font=('Helvetica', 15))

        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = function.get_todo('allinone/todos.txt')
            function.write_todos('allinone/todos.txt')
            window['todos'].update(values=todos)
            window['todo'].update(values='')
        case"Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()


