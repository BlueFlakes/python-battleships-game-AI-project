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
        for ship in self.ocean.ships: ship.ship_status()
        self.is_winner = self.ocean.is_every_ship_sunk()

        return self.is_winner

    def shot(self, enemy_ocean):
        proper_coordinates = False
        alphanumeric_dict = dict([[item for item in pair[::-1]] for pair in enumerate(self.ocean.alphabet_list[:])])

        while not proper_coordinates:
            coordinates = Ui.get_inputs(["First coordinate", "Second coordinate"], "Where do you want to shot?")
            proper_coordinates = Game.check_coordinates(coordinates, alphanumeric_dict)

        row = int(coordinates[1]) - 1
        column = alphanumeric_dict[coordinates[0].upper()]
        square = enemy_ocean.board[row][column]
        enemy_square = self.ocean.enemy_board[row][column]
        square.hit()
        if square.is_element_of_ship:
            enemy_square.is_element_of_ship = True
        enemy_square.hit()


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
