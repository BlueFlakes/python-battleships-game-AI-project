from ui import Ui
from square import Square
from ocean import Ocean


class Ship:

    def __init__(self, ship_name, row, column, direction):
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
        is_close = self.check_enviroment(board)
        print(is_close)
        if is_close is False:
            for i in range(self.size):
                try:
                    board[row][column].is_element_of_ship = True
                    self.squares.append(board[row][column])
                    if self.direction == "right":
                        column += 1
                    elif self.direction == "left":
                        column -= 1
                    elif self.direction == "up":
                        row -= 1
                    elif self.direction == "down":
                        row += 1
                except IndexError:
                    Ui.print_message("Ship can't be placed out of board!")
        else:
            print('NOPE!')

    def check_enviroment(self, board):
        temp_list = []
        end_row, end_column = self.set_ship_end(board)

        if self.direction == 'right' or self.direction == 'left':
            if self.direction == 'left':
                end_row, end_column = self.start_row, self.start_column

            for i in range(self.size + 2):
                for j in range(3):
                    temp_list.append(board[self.start_row + j - 1][self.start_column + i - 1])

        elif self.direction == 'up' or self.direction == 'down':
            if self.direction == 'up':
                end_row, end_column = self.start_row, self.start_column

            for i in range(self.size + 2):
                for j in range(3):
                    temp_list.append(board[self.start_row + i - 1][self.start_column + j - 1])

        is_close = True if True in [item.is_element_of_ship for item in temp_list] else False
        return is_close

    def set_ship_end(self, board):
        end_row = self.start_row
        end_column = self.start_column
        if self.direction == "right":
            end_column += (self.size - 1)
        elif self.direction == "left":
            end_column -= (self.size - 1)
        elif self.direction == "up":
            end_row -= (self.size - 1)
        elif self.direction == "down":
            end_row += (self.size - 1)

        return end_row, end_column


def main():
    baltyk = Ocean()
    ship1 = Ship('carrier', 2, 3, 'right')
    ship2 = Ship('carrier', 5, 4, 'right')
    ship3 = Ship('carrier', 2, 3, 'left')
    ship4 = Ship('carrier', 2, 4, 'right')
    ship5 = Ship('carrier', 1, 3, 'left')

    ship1.place_ship(baltyk.board)
    print(baltyk)
    ship2.place_ship(baltyk.board)
    print(baltyk)
    ship3.place_ship(baltyk.board)
    print(baltyk)
    ship4.place_ship(baltyk.board)
    print(baltyk)
    ship5.place_ship(baltyk.board)
    print(baltyk)




if __name__ == '__main__':
    main()
