import os
import ui


def main():
    option = float("inf")
    while not option == "3":
        print_menu()
        option = choose()


def print_menu():
    ui.display_screen("screens/menu.txt")


def choose():
    """
    Calls proper functions based on user's choice.

    Args:


    Returns:
        option: string
    """

    option = ui.get_inputs(["Please choose an option"], "")
    option = option[0]

    if option == "1":
        pass
    elif option == "2":
        ui.display_screen("screens/credits.txt", True)

    elif option == "3":
        print("Good bye!")

    return option


main()
