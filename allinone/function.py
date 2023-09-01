

FILEPATH = "allinone/todos.txt"


def get_todo(filepath=FILEPATH):
    with open("allinone/todos.txt", 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    todos = get_todo(FILEPATH)
    print(todos)

