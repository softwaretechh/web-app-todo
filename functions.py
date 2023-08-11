FILEPATH = "todos.txt"


def get_todos(filepath="todos.txt"):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        """Read a text file, stored and return d list of 
        to-do items-This is called Doc-string-it help us to know what our function does
        """
    return todos_local  # we used this at each
    # function calls at no 15,24,38,51. todos_local subsequently became todos.


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the to-do items list in the text file
    """
    with open(filepath, "w") as loca_file:
        loca_file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
