from square import Square


class Ocean:
    __board_size = 10

    def __init__(self):
        self.ships = []
        self.enemy_board = [[Square() for j in range(self.__board_size)] for i in range(self.__board_size)]
        self.board = [[Square() for j in range(self.__board_size)] for i in range(self.__board_size)]

    def __str__(self):
        board_to_display = ''
        board, enemy_board, row_index = self.__enumerate_alpha_index()

        for i in range(self.__board_size+1):
            row_board = [item.__str__() for item in board[i]]
            row_enemy_board = [item.__str__() for item in enemy_board[i]]
            longest_number = max([len(row) for row in row_index]) + 1
            space_amount = longest_number - len(str(i))

            board_to_display += row_index[i] + space_amount * ' ' + str(' '.join(row_board)) + (8 * ' ')
            board_to_display += row_index[i] + space_amount * ' ' + str(' '.join(row_enemy_board)) + '\n'

        return board_to_display

    def __enumerate_alpha_index(self):
        alpha = [chr(i) for i in range(65, 65 + self.__board_size)]
        enumerate_records = [' ' if i == 0 else str(i) for i in range(self.__board_size+2)]
        board = self.board[:]
        enemy_board = self.enemy_board[:]
        board.insert(0, alpha)
        enemy_board.insert(0, alpha)

        return board, enemy_board, enumerate_records

    def add_ship_to_ocean(self, ship):
        self.ships.append(ship)

    def is_every_ship_sunk(self):
        ships_condition = False if False in [ship.is_sunk for ship in self.ships] else True
        return ships_condition
