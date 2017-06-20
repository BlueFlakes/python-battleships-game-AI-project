from square import Square


class Ocean:
    __board_size = 10

    def __init__(self):
        self.ships = []
        self.enemy_board = [[Square() for j in range(self.__board_size)] for i in range(self.__board_size)]
        self.board = [[Square() for j in range(self.__board_size)] for i in range(self.__board_size)]

    def __str__(self):
        board_to_display = ''

        for i in range(self.__board_size):
            row_board = [item.__str__() for item in self.board[i]]
            row_enemy_board = [item.__str__() for item in self.enemy_board[i]]

            board_to_display += (str(' '.join(row_board)) + (8 * ' ') +
                                 str(' '.join(row_enemy_board)) + '\n')

        return board_to_display

    def update_board(self):
        pass

    def add_ship_to_board(self, ship):
        pass

    def is_every_ship_sunk(self):
        pass


def main():
    baltic = Ocean()

    print(baltic)


if __name__ == '__main__':
    main()
