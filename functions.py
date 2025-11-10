def get_todos(filepath ="todos.txt"):
    """Reads a text file and returns the list
    of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos( todos_arg,filepath="todos.txt"):
# in the above statement filepath is a default argument and thats why its position is 2nd since a default arg cannot come before a regular parameter
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)