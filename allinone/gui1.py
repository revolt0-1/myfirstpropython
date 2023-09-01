import PySimpleGUI as sg
import function

labels = ('Type in TO-DO:', 'FILE:')
size = max(map(len, labels))

font = ('Courier New', 11)
sg.theme('DarkBlue4')
sg.set_options(font=font)

layout = [
    [sg.Text(label, size=size), sg.Input(key=label.split()[0])]
    for label in labels
] + [
    [sg.Push(), sg.Button('ADD')]
]
window = sg.Window('TO-DO APP', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "ADD":
        todos = function.get_todo()
        new_todo = values['Typein'] + "\n"  # 'Typein' should match the key of your input element
        todos.append(new_todo)
        function.write_todos(todos)

window.close()
