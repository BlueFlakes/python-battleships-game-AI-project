from random import randint
from time import sleep

from Interface.ui import Ui
from Interface.hall_of_fame import HallOfFame
from models.player import Player


class Game:
    """
    Constructs Game object, def multiple methods for it manipulation.
    """
    current_game = None
    """
    Instance Attributes

    self.type
    data: string
        description: Contains information about type of game: singleplayer, multiplayer, simulation.

    self.player1
    data: Player object
        description: Contains first player object

    self.player2
    data: Player object
        description: Contains first player object

    self.is_over
    data: boolean
        description: Contains True if one of the players wins, otherwise contains False.

    self.player_in_round
    data: Player object
        description: Contains Player object which is currently shooting
    """

    def __init__(self, player1, player2):
        self.type = "Multi player"
        self.player1 = player1
        self.player2 = player2
        self.is_over = None
        self.player_in_round = None

    def __init__(self, player, computer):
        self.type = "Single Player"
        self.player1 = player
        self.player2 = computer
        self.is_over = None
        self.player_in_round = None

    def __init__(self, computer1, computer2):
        self.type = "Simulation"
        self.player1 = computer1
        self.player2 = computer2
        self.is_over = None
        self.player_in_round = None

    def is_game_over(self):
        """
        Returns True if someone wins, otherwise returns False

        Returns:
        is_over: boolean

        """
        if self.player1.check_status() is True or self.player2.check_status() is True:
            is_over = True
        else:
            is_over = False

        return is_over

    def start_game(self):
        """
        Calls set_ships function for both players, and draws which one will shot first.

        Returns:
        -------
        None

        """
        first_player_number = randint(1, 2)
        if first_player_number == 1:
            self.player_in_round = self.player1

        else:
            self.player_in_round = self.player2

        self.player1.set_ships()
        self.player2.set_ships()

        self.turn()
        exit = Ui.get_inputs(["Press any number to exit"], "")

    def set_first_player(self):
        """
        Set first player.

        Returns:
        -------
        None
        """

        first_player_number = randint(1, 2)
        if first_player_number == 1:
            self.player_in_round = self.player1

        else:
            self.player_in_round = self.player2

    def player_switch(self):
        """
        Switch players

        Returns:
        -------
        None
        """

        if self.player_in_round is self.player1:
            self.player_in_round = self.player2
        else:
            self.player_in_round = self.player1

    def turn(self):

        while not self.is_over:
            Ui.print_message(self.player_in_round.name)
            Ui.print_message(self.player_in_round.ocean)
            if self.player_in_round == self.player1:
                shot_done = False
                while not shot_done:
                    shot_done = self.player_in_round.shot(self.player2.ocean)
            else:
                shot_done = False
                while not shot_done:
                    shot_done = self.player_in_round.shot(self.player1.ocean)
            sleep(0.00)
            self.is_over = self.is_game_over()

            self.player_switch()

        if self.is_over:
            print(self.player1)
            print(self.player2)

        if isinstance(self.player1, Player) or isinstance(self.player2, Player):
            self.add_player_to_highscore()

    @classmethod
    def check_coordinates(cls, coordinates, alphanumeric_dict):
        """
        Returns True if player choose a letter between A and J, otherwise returns False.

        Parameters
        ---------
        coordinates: list
            list contain row and column
        alphanumeric_dict: dict

        Returns
        --------
        True or False
        """

        if coordinates[0].isdigit():
            if coordinates[1].upper() in alphanumeric_dict and int(coordinates[1]) in range(1, 11):
                return True
            else:
                return False
        else:
            return False

    def add_player_to_highscore(self):
        """
        At the end of the game, if one of the player's was a Player
        object and he won, saves data about him to .csv file.

        Returns
        --------
        None
        """
        if not self.player1.is_loser and isinstance(self.player1, Player):
            name = self.player1.name
            counted_shots = self.player1.counted_shots

        elif not self.player2.is_loser and isinstance(self.player2, Player):
            name = self.player2.name
            counted_shots = self.player2.counted_shots

        HallOfFame.save_to_file('Interface/hall_of_fame.csv', name, counted_shots)
