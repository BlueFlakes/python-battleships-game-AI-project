from random import randint
from time import sleep

from Interface.ui import Ui


class Game:
    current_game = None

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
        if self.player1.check_status() is True or self.player2.check_status() is True:
            is_over = True
        else:
            is_over = False

        return is_over

    def start_game(self):
        first_player_number = randint(1, 2)
        if first_player_number == 1:
            self.player_in_round = self.player1

        else:
            self.player_in_round = self.player2

        self.player1.set_ships()
        self.player2.set_ships()

        self.turn()

    def set_first_player(self):
        first_player_number = randint(1, 2)
        if first_player_number == 1:
            self.player_in_round = self.player1

        else:
            self.player_in_round = self.player2

    def player_switch(self):
        if self.player_in_round is self.player1:
            self.player_in_round = self.player2
        else:
            self.player_in_round = self.player1

    def turn(self):
        while not self.is_over:
            Ui.print_message(self.player_in_round.name)
            Ui.print_message(self.player_in_round.ocean)
            if self.player_in_round == self.player1:
                self.player_in_round.shot(self.player2.ocean)
            else:
                self.player_in_round.shot(self.player1.ocean)
            sleep(0.00)
            self.is_over = self.is_game_over()

            self.player_switch()

        if self.is_over:
            print(self.player1)
            print(self.player2)
        exit()

    @classmethod
    def check_coordinates(cls, coordinates, alphanumeric_dict):
        if coordinates[0].isdigit():
            if coordinates[1].upper() in alphanumeric_dict and int(coordinates[1]) in range(1, 11):
                return True
            else:
                return False
        else:
            return False
