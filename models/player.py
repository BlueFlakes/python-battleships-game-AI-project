from Interface.ui import Ui
from models.game import Game
from models.ocean import Ocean
from models.ship import Ship


class Player:

    def __init__(self, name):
        self.name = name
        self.is_loser = False
        self.ocean = Ocean()

    def __str__(self):
        if self.is_loser is True:
            return "{} is a loser!".format(self.name)
        else:
            return "{} has won the game!".format(self.name)

    def check_status(self):
        self.is_loser = self.ocean.is_every_ship_sunk()

        return self.is_loser

    def shot(self, enemy_ocean):
        proper_coordinates = False
        alphanumeric_dict = dict([[item for item in pair[::-1]] for pair in enumerate(self.ocean.alphabet_list[:])])

        coordinates = Ui.get_inputs(["Row", "Column"], "Where do you want to shot?")

        row = int(coordinates[0]) - 1
        column = alphanumeric_dict[coordinates[1].upper()]
        square = enemy_ocean.board[row][column]
        enemy_square = self.ocean.enemy_board[row][column]
        square.hit()
        if square.is_element_of_ship:
            enemy_square.is_element_of_ship = True
        enemy_square.hit()

    def set_ships(self):
        alphanumeric_dict = dict([[item for item in pair[::-1]] for pair in enumerate(self.ocean.alphabet_list[:])])

        for name, lenght in Ship.sizes.items():
            is_close = True
            while is_close:
                ship_specification = Ui.get_inputs(["Row", "Column", "Direction"],
                                                   "\nPlease place {} which length is {}".format(name, lenght))
                row = int(ship_specification[0]) - 1
                column = alphanumeric_dict[ship_specification[1].upper()]

                ship = Ship(name, row, column, ship_specification[2])
                is_close = ship.check_enviroment(self.ocean.board)
                ship.place_ship(self.ocean.board)
                Ui.print_message(self.ocean)
            self.ocean.add_ship_to_ocean(ship)

    def shot(self, enemy_ocean, coord):
        proper_coordinates = False
        alphanumeric_dict = dict([[item for item in pair[::-1]] for pair in enumerate(self.ocean.alphabet_list[:])])

        coordinates = coord

        row = int(coordinates[0]) - 1
        column = alphanumeric_dict[coordinates[1].upper()]
        square = enemy_ocean.board[row][column]
        enemy_square = self.ocean.enemy_board[row][column]
        square.hit()
        if square.is_element_of_ship:
            enemy_square.is_element_of_ship = True
        enemy_square.hit()