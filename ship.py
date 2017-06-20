from ui import Ui
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
            Ui.print_message("Provided ship name is wrong.")

        return size

    def check_status(self):
        is_hit_statuses = [square.is_hit for square in self.squares]

        self.is_sunk = False if False in is_hit_statuses else True

    def place_ship(self, board):
        row = self.start_row
        column = self.start_column

        for i in range(self.size):
            try:
                is_close = check_enviroment(board)
                board[row, column].is_element_of_ship = True
                self.squares.append(board[row, column])

                if self.direction == "right":
                    column += 1
                if self.direction == "left":
                    column -= 1
                if self.direction == "up":
                    row -= 1
                if self.direction == "down":
                    row += 1

            except IndexError:
                Ui.print_message("Ship can't be placed out of board!")

            return board

    def check_enviroment(board):
        ship_start = board[self.start_row, start_column]

        if self.direction == "right":
            column += 1
        if self.direction == "left":
            column -= 1
        if self.direction == "up":
            row -= 1
        if self.direction == "down":
            row += 1
