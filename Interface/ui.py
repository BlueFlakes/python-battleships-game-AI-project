import os


class Ui:
    @classmethod
    def get_inputs(cls, list_labels, title):
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
                check = True
                while check:
                    user_input = input(question + ': ')
                    if len(str(user_input)) == 0:
                        check = True
                        cls.print_error_message('It can not be an empty, write something :)')

                    elif question == 'Row' or question == 'Column':
                        if user_input.isdigit():
                            check = False
                        else:
                            cls.print_error_message('It is not a number, try again!')

                    elif question == 'Level':
                        if user_input == 'Easy' or user_input == 'Medium' or user_input == 'Hard':
                            check = False
                        else:
                            cls.print_error_message('3 option to choose: Empty, Medium, Hard')

                    elif question == 'Name':
                        if user_input.isalpha():
                            check = False
                        else:
                            cls.print_error_message('Rly?! Your name contain numbers or special chars? Are you a robot?')

                    elif question == 'Direction':
                        if user_input == 'up' or user_input == 'down' or user_input == 'left' or user_input == 'right':
                            check = False
                        else:
                            cls.print_error_message('4 option to choose: up, down, left, right')
                    else:
                        check = False
                inputs.append(user_input)

        elif len(list_labels) == 1:
            check = True
            while check:
                user_input = input(list_labels[0] + ':')
                if len(str(user_input)) == 0:
                    check = True
                    cls.print_error_message('It can not be an empty, write something :)')
                else:
                    check = False
            inputs.append(user_input)

        return inputs

    @classmethod
    def display_screen(cls, file_name, wait_for_exit=False):
        os.system("clear")
        with open(file_name, "r") as f:
            print(f.read())

        if wait_for_exit is True:
            option = float("inf")
            while not option == "0":
                option = Ui.get_inputs([""], "")
                option = option[0]

    @classmethod
    def print_error_message(cls, message):
        print(message)

    @classmethod
    def print_message(cls, message):
        print(message)
