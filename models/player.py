from Interface.ui import Ui
from models.game import Game
from models.ocean import Ocean
from models.ship import Ship


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
        proper_coordinates = False

        while not proper_coordinates:
            coordinates = Ui.get_inputs(["First coordinate", "Second coordinate"], "Where do you want to shot?")
            proper_coordinates = Game.check_coordinates(coordinates, self.ocean.alpha)

        row = int(coordinates[1]) - 1
        column = self.ocean.alpha[coordinates[0].upper()]
        square = self.ocean.enemy_board[row][column]
        square.hit()

    def set_ships(self):
        for key, value in Ship.sizes.items():
            is_close = True
            while is_close:
                ship_specification = Ui.get_inputs(["Row", "Column", "Direction"],
                                                   "\nPlease place {} which length is {}".format(key, value))
                ship = Ship(key, ship_specification[0], ship_specification[1], ship_specification[2])
                is_close = ship.check_enviroment(self.ocean.board)
                ship.place_ship(self.ocean.board)
                Ui.print_message(self.ocean)
