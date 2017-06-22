from Interface.ui import Ui
from models.computer import Computer
from models.game import Game
from models.player import Player


def main():
    option = float("inf")
    while not (option == "0"):
        Ui.display_screen("screens/menu.txt")
        option = choose()


def choose():
    """
    Calls proper functions based on user's choice.

    Returns:
        option: string
    """
    check = True
    while check:

        option = Ui.get_inputs(["Please choose an option"], "")
        option = option[0]

        if option == "1":
            start_singleplayer()
            check = False

        elif option == "2":
            start_multiplayer()
            check = False

        elif option == "3":
            start_simulation()
            check = False

        elif option == "4":
            Ui.display_screen("screens/credits.txt", True)
            check = False

        elif option == "0":
            Ui.print_message("Good bye!")
            check = False
        else:
            check = True
            Ui.print_error_message('You know there is no option like that, come on!')

    return option


def start_singleplayer():
    data = Ui.get_inputs(["Name", "Level"], "Please provide your name and choose difficulty level")
    player1 = Player(data[0])

    level = data[1]
    computer = Computer(level)

    gameplay = Game(player1, computer)
    gameplay.start_game()


def start_multiplayer():
    players = Ui.get_inputs(["First player's name", "Second player's name"], "Please provide your names")
    player1 = Player(players[0])
    player2 = Player(players[1])

    gameplay = Game(player1, player2)
    gameplay.start_game()


def start_simulation():
    for level in Computer.allowed_levels:
        Ui.print_message("Option: {} ".format(level))
    proper_level = False
    while not proper_level:
        levels = Ui.get_inputs(["Level", "Level"], "Choose computer\'s level")
        comp1_level = levels[0]
        comp2_level = levels[1]
        if level in Computer.allowed_levels:
            proper_level = True

    computer1 = Computer(comp1_level)
    computer2 = Computer(comp2_level)
    computer2.name = "Computer2"

    gameplay = Game(computer1, computer2)
    gameplay.start_game()


if __name__ == "__main__":
    main()
