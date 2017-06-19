import ui
from ocean import Ocean


class Player:

    def __init__(self, name):
        self.name = name
        self.is_winner = False
        self.ocean = Ocean()

    def __str__(self):
        if self.is_winner is True:
            return "{} has won the game!".format(self.name)
        else:
            return "{} is a loser!".format(self.name)

    def check_status(self):
        ships_statuses = [ship.is_sunk for ship in self.ocean.ships]

        self.is_winner = False if False in ships_statuses else True

    def shot(self):
        coordinates = ui.get_inputs(["First coordinate", "Second coordinate"], "Where do you want to shot?")
        coordinates = str(coordinates[0]) + str(coordinates[1])

        self.ocean.shot(coordinates)
