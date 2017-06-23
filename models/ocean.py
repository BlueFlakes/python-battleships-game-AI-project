from models.square import Square


class Ocean:
    """
    Constructs a Ocean object, def multiple methods for it manipulation, returns it as a formatted string
    """

    __board_size = 10
    # Creating list with alphabet, A - amount of letters for columns
    # it's used to interpret alphanumeric coordinates
    alphabet_list = [chr(i) for i in range(65, 65 + __board_size)]

    def __init__(self):
        """
        Creates Ocean object

        Instance Attributes:
        -------------------
        * ships
            * data: list
            * description: list of ship objects

        * board
            * data: list
            * description: list of nested lists, contains map for the battleship game :)

        * enemy_board
            * data: list
            * description: list of nested lists, same as *board*
        """

        self.ships = []
        self.enemy_board = [[Square() for j in range(self.__board_size)] for i in range(self.__board_size)]
        self.board = [[Square() for j in range(self.__board_size)] for i in range(self.__board_size)]

    def __str__(self):
        """
        Make string with both boards, it will be use to display boards on screen.

        Returns
        -------
        board_to_display: string
            String with player's *board* and *enemy_board*
        """
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
        """
        Enumarating both boards upper indexes with aplha from A to J.

        Returns:
        board: list
            List with upper indexes
        enemy_board: list
            List with upper indexes
        enumerate_records: str
        """

        enumerate_records = [' ' if i == 0 else str(i) for i in range(self.__board_size+2)]
        board = self.board[:]
        enemy_board = self.enemy_board[:]
        board.insert(0, self.alphabet_list)
        enemy_board.insert(0, self.alphabet_list)

        return board, enemy_board, enumerate_records

    def add_ship_to_ocean(self, ship):
        """
        Add object Ship to object Ocean.

        Parameters
        ----------
        ship: :obj:
            Object of Ship Class.

        Returns
        -------
        None
        """

        self.ships.append(ship)

    def is_every_ship_sunk(self):
        """
        Checks if every player's ship is sunk.

        Returns
        -------
        ships_condition: bool
            Return True if all ships in map are sunks, else: False.
        """

        ships_condition = False if False in [ship.check_status() for ship in self.ships] else True

        return ships_condition
