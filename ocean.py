from square import Square


class Ocean:
    __board_size = 10

    def __init__(self):
        self.ships = []
        self.enemy_board = []
        self.board = []

    def create_board(self):
        new_board = []

        for x in range(self.__board_size):
            temp = []

            for y in range(self.__board_size):
                temp.append(Square(x, y))

            new_board.append(temp)

        return new_board

    def __str__(self):
        board_to_display = ''
        for i in range(len(temp1)):
            board_to_display += str(' '.join(temp1[i])) + (5 * ' ') + str(' '.join(temp2[i])) + '\n'

        return board_to_display

    def update_board(self, ship):
        pass

    def is_every_ship_sunk(self):
        pass


def main():
    baltic = Ocean()
    baltic.create_board()
    print(baltic)
    baltic.board = baltic.create_board()
    print(baltic.board)


if __name__ == '__main__':
    main()
