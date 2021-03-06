from Interface.ui import Ui
from models.square import Square
from models.ocean import Ocean


class Ship:
    """
    Constructs Ship object, def multiple methods for it manipulation.

    sizes: dict
        Key: ship name
        Value: ship size
    """

    sizes = {"carrier": 5, "battleship": 4, "cruiser": 3, "submarine": 3, "destroyer": 2}

    def __init__(self, ship_name, row, column, direction):
        """
        Constructs Ship object.

        Parameters
        ------------
        ship_name: string
        row: integer
        column: string
            Letters from A to J
        direction: string
            Choice beetwen: left, right, up, down.

        __Instance Attributes__
        ------------

        * self.squares
          - data: list
          - description: list of square() objects

        * self.name
          - data: string
          - description: type of ship, i. e. carrier, cruiser

        * self.size
          - data: integer
          - description: lenght of size list

        * self.direction
          - data: string
          - description: contains string with direction of ship: "up", "down, "left", "right"

        * self.is_sunk
          - data: boolean
          - description: contains True if all squares elements are hit, otherwise contains False

        * self.start_column
          - data: integer
          - description: one of coordinates which decide where ship will be placed

        * self.start_row
          - data: integer
          - description: one of coordinates which decide where ship will be placed

        """
        self.name = ship_name.lower()
        self.is_sunk = False
        self.start_column = column
        self.start_row = int(row)
        self.direction = direction.lower()

        self.size = self.set_size()
        self.squares = []

    def set_size(self):
        """
        Sets *size* attribute based on name of ship.

        Returns
        -------
        size: :obj:

        """

        try:
            size = Ship.sizes[self.name]
        except KeyError:
            Ui.print_message("Provided ship name is wrong.")

        return size

    def check_status(self):
        """
        Checks if all squares of ship are hit. If yes, sets *self.is_sunk* to True.

        Returns:
        --------
        self.is_sunk: boolean
        """

        is_hit_statuses = [square.is_hit for square in self.squares]

        self.is_sunk = False if False in is_hit_statuses else True

        return self.is_sunk

    def place_ship(self, board):
        """
        Changes correct square's *is_element_of_ship* attribute to True

        Parameters
        -------
        board: :obj:

        Returns:
        -------
        None
        """
        row = self.start_row
        column = self.start_column
        is_close = self.check_enviroment(board)

        if is_close is False:
            for i in range(self.size):
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

        else:
            Ui.print_message("Can\'t place a ship here!\n")

    def check_enviroment(self, board):
        """
        Returns True if there is another ship close to the new ship position, else returns False.

        Parameters
        ----------
        board: :obj:

        Returns:
        ----------
        is_close: boolean
        """

        end_row, end_column = self.set_ship_end(board)
        if end_row == "too far" or end_column == "too far":
            is_close = True
        else:
            squares_around = self.set_squares_around(board, end_row, end_column)

            if len(squares_around) > 0:
                is_close = True if True in [item.is_element_of_ship for item in squares_around] else False
            else:
                is_close = True

        return is_close

    def set_squares_around(self, board, end_row, end_column):
        """
        Returns list of *Square* objects which are around ship's position.

        Parameters:
        -----------
        board: :obj:
        end_row: int
        end_column: int

        Returns:
        -----------
        squares_around: list

        """

        squares_around = []

        for i in range(self.size + 2):
            for j in range(3):
                try:
                    if self.direction == 'right':
                        squares_around.append(board[self.start_row + j - 1][self.start_column + i - 1])
                    elif self.direction == 'left':
                        squares_around.append(board[self.start_row + j - 1][self.start_column - i + 1])
                    elif self.direction == 'down':
                        squares_around.append(board[self.start_row + i - 1][self.start_column + j - 1])
                    elif self.direction == "up":
                        squares_around.append(board[self.start_row - i + 1][self.start_column + j - 1])

                except IndexError:
                    continue

        return squares_around

    def set_ship_end(self, board):
        """
        Returns end row and end column of ship.

        Parameters:
        -----------
        board: :obj:

        Returns:
        -----------
        end_row: int
        edn_column: int

        """
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

        if end_row < 0 or end_row > 9:
            end_row = "too far"
        if end_column < 0 or end_column > 9:
            end_column = "too far"

        return end_row, end_column
