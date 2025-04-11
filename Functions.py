
def get_tasks(filepath="app.txt"):
    """Read a text file and return the list of items"""
    with open(filepath, "r") as file_local:
        tasks_local = file_local.readlines()
    return tasks_local


def write_tasks(tasks_arg,filepath = "app.txt"):
    """Write the list of tasks in the text file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(tasks_arg)


if __name__ == "__App__":
    print("Hello")

