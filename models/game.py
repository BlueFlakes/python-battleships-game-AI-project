from random import randint
from time import sleep

from Interface.ui import Ui


class Game:
    current_game = None

    def __init__(self, player1, player2):
        self.type = "Multi player"
        self.player1 = player1
        self.player2 = player2
        self.is_over = self.is_game_over()
        self.player_in_round = None

    def __init__(self, player, computer):
        self.type = "Single Player"
        self.player1 = player
        self.player2 = computer
        self.is_over = self.is_game_over()
        self.player_in_round = None

    def __init__(self, computer1, computer2):
        self.type = "Simulation"
        self.player1 = computer1
        self.player2 = computer2
        self.is_over = self.is_game_over()
        self.player_in_round = None

    def is_game_over(self):
        if self.player1.check_status() is True or self.player2.check_status() is True:
            return True

    def start_game(self):
        first_player_number = randint(1, 2)
        if first_player_number == 1:
            self.player_in_round = self.player1

        else:
            self.player_in_round = self.player2

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
            Ui.print_message(self.player_in_round.name + "     " + "")
            Ui.print_message(self.player_in_round.ocean)
            self.player_in_round.shot()
            sleep(3)
            if self.is_over:
                Ui.print_message("{} won".format(self.player_in_round.name))
                break
            self.player_switch()

    @classmethod
    def check_coordinates(cls, coordinates):
        if coordinates[0].isdigit() and coordinates[1].isdigit():
            if int(coordinates[0]) in range(1, 10) and int(coordinates[1]) in range(1, 10):
                return True
            else:
                return False
        else:
            return False
