import os


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels: list of strings - labels of inputs
        title: string - title of the "input section"

    Returns:
        List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    if type(list_labels) == list:
        print(title)

        for question in list_labels:
            user_input = input(question+': ')
            inputs.append(user_input)

    elif len(list_labels) == 1:
        user_input = input(list_labels[0]+':')
        inputs.append(user_input)

    return inputs


def display_screen(file_name, wait_for_exit=False):
    os.system("clear")
    with open(file_name, "r") as f:
        print(f.read())

    if wait_for_exit is True:
        option = float("inf")
        while not option == "0":
            option = get_inputs([""], "")
            option = option[0]
