class Ocean:
    __board_size = 10

    def __init__(self):
        self.ships = []
        self.enemy_board = []
        self.board = []

    def create_board(self):
        pass

    def __str__(self):
        board_to_display = ''
        for row in self.board:
            for cell in row:
                board_to_display += str(cell)
            board_to_display += "\n"
        return board_to_display


def main():
    ocean = Ocean()
    print(ocean.create_board())
    print(ocean)


if __name__ == '__main__':
    main()
