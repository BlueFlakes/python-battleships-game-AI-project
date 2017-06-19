import os
import ui
from player import Player


def main():
    option = float("inf")
    while not (option == "3" or option == "1"):
        print_menu()
        option = choose()

    if option == "1":
        start_gameplay()


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


def start_gameplay():
    """
    Main game loop, which ends when one of the player wins.

    Returns:
        None
    """

    names = ui.get_inputs(["Player1 name", "Player2 name"], "Please provide your names")

    player1 = Player(names[0])
    player2 = Player(names[1])

    while not (player1.is_winner or player2.is_winner):
        player1.shot()
        player2.shot()

    print(player1)
    print(player2)


if __name__ = "__main__":
    main()
