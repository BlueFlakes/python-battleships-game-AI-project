import ui
from game import Game
from computer import Computer
from player import Player


def main():
    option = float("inf")
    while not (option == "0"):
        ui.display_screen("screens/menu.txt")
        option = choose()


def choose():
    """
    Calls proper functions based on user's choice.

    Returns:
        option: string
    """

    option = ui.get_inputs(["Please choose an option"], "")
    option = option[0]

    if option == "1":
        start_singleplayer()

    elif option == "2":
        start_multiplayer()

    elif option == "3":
        start_simulation()

    elif option == "4":
        ui.display_screen("screens/credits.txt", True)

    elif option == "0":
        ui.print_message("Good bye!")

    return option


def start_singleplayer():
    # ui.display_screen("screens/level.txt")
    data = ui.get_inputs(["Name", "Level"], "Please provide your name and choose difficulty level")
    player1 = Player(data[0])

    level = data[1]
    computer = Computer(level)

    gameplay = Game(player1, computer)
    gameplay.start_game()


def start_multiplayer():
    players = ui.get_inputs(["First player's name", "Second player's name"], "Please provide your names")
    player1 = Player(players[0])
    player2 = Player(players[1])

    gameplay = Game(player1, player2)
    gameplay.start_game()


def start_simulation():
    levels = ui.get_inputs(["Computer's level"], "Choose computers level")
    level = levels[0]

    computer1 = Computer(level)
    computer2 = Computer(level)

    gameplay = Game(computer1, computer2)
    gameplay.start_game()


if __name__ == "__main__":
    main()
