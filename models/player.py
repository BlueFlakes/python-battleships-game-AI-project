from Interface.ui import Ui
from models.ocean import Ocean
from models.ship import Ship


class Player:
    """
    Constructs Player object, def multiple methods for it manipulation, returns it as a formatted string.
    """

    def __init__(self, name):
        """
        Constructs Player object.

        Parameters
        ----------
        name: str

        __Instance Attributes__
        -----------------------

        * name
          - data: string
          - description: name of the player

        * is_loser
          - data: boolean
          - description: Is True if player lose, otherwise is False.

        * ocean
          - data: Ocean()
          - description: Ocean instance

        * counted_shots
          - data: int
          - description: Shots used by player
        """

        self.name = name
        self.is_loser = False
        self.ocean = Ocean()
        self.counted_shots = 0

    def __str__(self):
        """
        Returns string with information about win or lose of the player, based on attribute *is_loser*.

        Returns
        -------
        board_to_display: string
        """

        if self.is_loser is True:
            return "{} is a loser!".format(self.name)
        else:
            return "{} has won the game!".format(self.name)

    def check_status(self):
        """
        Sets *is_loser* attribute to True if all player's ships are sunk, otherwise sets False.

        Returns
        -------
        self.is_loser: boolean
        """

        self.is_loser = self.ocean.is_every_ship_sunk()

        return self.is_loser

    def shot(self, enemy_ocean):
        """
        Takes input with coordinates to shot from player, then checks if player can shot there.
        - If yes, changes *is_hit* attribute of correct square to True.
        - If no, asks for coordinates again.

        Parameters
        ----------
        enemy_ocean: :obj:
            Object of Ocean class.

        Returns
        -------
        board_to_display: boolean
        """
        proper_coordinates = False
        alphanumeric_dict = dict([[item for item in pair[::-1]] for pair in enumerate(self.ocean.alphabet_list[:])])

        coordinates = Ui.get_inputs(["Row", "Column"], "Where do you want to shot?")

        row = int(coordinates[0]) - 1
        column = alphanumeric_dict[coordinates[1].upper()]
        square = enemy_ocean.board[row][column]
        enemy_square = self.ocean.enemy_board[row][column]
        if not square.is_hit:
            square.hit()
            if square.is_element_of_ship:
                enemy_square.is_element_of_ship = True
            enemy_square.hit()
            self.counted_shots += 1
            return True
        else:
            return False

    def set_ships(self):
        """
        - Asks player for coordinates to place ships on his ocean, checks if it's possible.
          If yes, places ship on the provided coordinates.
          If no, asks for coordinates again.

        Returns:
        --------
        None
        """

        alphanumeric_dict = dict([[item for item in pair[::-1]] for pair in enumerate(self.ocean.alphabet_list[:])])

        for name, lenght in Ship.sizes.items():
            is_close = True
            while is_close:
                ship_specification = Ui.get_inputs(["Row", "Column", "Direction"],
                                                   "\nPlease place {} which length is {}".format(name, lenght))
                row = int(ship_specification[0]) - 1
                column = alphanumeric_dict[ship_specification[1].upper()]

                ship = Ship(name, row, column, ship_specification[2])
                is_close = ship.check_enviroment(self.ocean.board)
                ship.place_ship(self.ocean.board)
                Ui.print_message(self.ocean)
            self.ocean.add_ship_to_ocean(ship)
