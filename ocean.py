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

        for i in range(self.__board_size):
            row_board = [item.__str__() for item in self.board[i]]
            row_enemy_board = [item.__str__() for item in self.enemy_board[i]]
            longest_number = len(str(self.__board_size)) + 2
            space_amount = longest_number - len(str(i+1))

            board_to_display += str(i + 1) + space_amount * ' ' + str(' '.join(row_board)) + (8 * ' ')
            board_to_display += str(i + 1) + space_amount * ' ' + str(' '.join(row_enemy_board)) + '\n'

        return board_to_display

    def update_board(self, ship):
        pass

    def is_every_ship_sunk(self):
        pass


def main():
    baltic = Ocean()
    baltic.create_board()

    baltic.board = baltic.create_board()
    baltic.enemy_board = baltic.create_board()

    print(baltic)


if __name__ == '__main__':
    main()
