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

        print(title)

        if len(list_labels) > 1:
            for question in list_labels:
                correct_answer = False
                while not correct_answer:
                    user_answer = input(question + ': ')
                    correct_answer = cls.check_answer(question, user_answer)
                inputs.append(user_answer)

        elif len(list_labels) == 1:
            question = list_labels[0]
            correct_answer = False
            while not correct_answer:
                user_answer = input(question + ': ')
                correct_answer = cls.check_characters(user_answer, False)
            inputs.append(user_answer)

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

    @classmethod
    def check_answer(cls, question, user_answer):
        correctness = False
        user_answer = user_answer.lower()

        if len(user_answer) == 0:
            correctness = False
            cls.print_error_message('It can not be an empty, write something :)')

        elif question == 'Row':
            correctness = cls.check_characters(user_answer, False)
            if correctness is True:
                if int(user_answer) > 10 or int(user_answer) < 1:
                    cls.print_message("Please enter number between 1 and 10!")
                    correctness = False

        elif question == 'Column':
            correctness = cls.check_characters(user_answer, True)
            # Check column method needs to be sure answer is alpha only
            if correctness is True:
                correctness = cls.check_column(user_answer)

        elif 'name' in question.lower():
            correctness = cls.check_characters(user_answer, True)

        elif question == 'Level':
            if user_answer == 'easy' or user_answer == 'medium' or user_answer == 'hard':
                correctness = True
            else:
                cls.print_error_message('3 option to choose: Easy, Medium, Hard')

        elif question == 'Direction':
            if user_answer == 'up' or user_answer == 'down' or user_answer == 'left' or user_answer == 'right':
                correctness = True
            else:
                cls.print_error_message('4 option to choose: up, down, left, right')
        else:
            correctness = False

        return correctness

    @classmethod
    def check_characters(cls, user_answer, letters=True):
        correctness = False

        if letters is True:
            if user_answer.isalpha():
                correctness = True
            else:
                cls.print_error_message('Please enter letters only!')

        else:
            if user_answer.isdigit():
                correctness = True
            else:
                cls.print_error_message('Please enter numbers only!')

        return correctness

    @classmethod
    def check_column(cls, user_answer):
        if len(user_answer) > 1:
            correctness = False
            cls.print_error_message("Please enter one character only!")

        elif ord(user_answer) < 97 or ord(user_answer) > 106:
            correctness = False
            cls.print_error_message("Please enter letters between A and J!")
        else:
            correctness = True

        return correctness
