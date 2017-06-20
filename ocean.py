from square import Square

class Ocean:
    __board_size = 10

    def __init__(self):
        self.ships = []
        self.shooted_ships = []
        self.board = []

    def create_board(self):
        for x in range(self.__board_size):
            temp = []

            for y in range(self.__board_size):
                temp.append(Square(x, y))

            self.board.append(temp)

def main():
    baltic = Ocean()
    baltic.create_board()


if __name__ == "__main__":
    main()
