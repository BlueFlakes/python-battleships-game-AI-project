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

    option = Ui.get_inputs(["Please choose an option"], "")
    option = option[0]

    if option == "1":
        start_singleplayer()

    elif option == "2":
        start_multiplayer()

    elif option == "3":
        start_simulation()

    elif option == "4":
        Ui.display_screen("screens/credits.txt", True)

    elif option == "0":
        Ui.print_message("Good bye!")

    return option


def start_singleplayer():
    # ui.display_screen("screens/level.txt")
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
        levels = Ui.get_inputs(["Computer's level"], "Choose computers level")
        level = levels[0]
        if level in Computer.allowed_levels:
            proper_level = True

    computer1 = Computer(level)
    computer2 = Computer(level)
    computer2.name = "Computer2"

    gameplay = Game(computer1, computer2)
    gameplay.start_game()


if __name__ == "__main__":
    main()
