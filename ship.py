import ui
from square import Square


class Ship:

    def __init__(self, ship_name, column, row, direction):
        self.name = ship_name.lower()
        self.is_sunk = False
        self.start_column = int(column)
        self.start_row = int(row)
        self.direction = direction.lower()

        self.size = self.set_size()
        self.squares = []

    def set_size(self):
        sizes = {"carrier": 5, "battleship": 4, "cruiser": 3, "submarine": 3, "destroyer": 2}

        try:
            size = sizes[self.name]
        except KeyError:
            ui.print_message("Provided ship name is wrong.")

        return size

    def check_status(self):
        is_hit_statuses = [square.is_hit for square in self.squares]

        self.is_sunk = False if False in is_hit_statuses else True

    def place_ship(self, board):

        for i in range(self.size):
            board[self.start_row, self.start_column].is_element_of_ship = True
            self.squares.append(board[self.start_row, self.start_column])

            if self.direction == "right":
                self.start_column += 1
            if self.direction == "left":
                self.start_column -= 1
            if self.direction == "up":
                self.start_row -= 1
            if self.direction == "down":
                self.start_row += 1

            return board
