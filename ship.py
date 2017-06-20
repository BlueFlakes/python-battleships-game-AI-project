import ui
from square import Square


class Ship:

    def __init__(self, ship_name, column, row):
        self.name = ship_name.lower()
        self.is_horizontal = False
        self.is_sunk = False
        self.start_column = int(column)
        self.start_row = int(row)

        self.squares_list = self.set_size()

    def set_size(self):
        sizes = {"carrier": 5, "battleship": 4, "cruiser": 3, "submarine": 3, "destroyer": 2}

        try:
            size = sizes[self.name]
        except KeyError:
            ui.print_message("Provided ship name is wrong.")

        return [Square(row, self.start_row, self.start_column) for i in range(size)]

    def check_status(self):
        is_hit_statuses = [square.is_hit for square in self.squares_list]

        self.is_sunk = False if False in is_hit_statuses else True
