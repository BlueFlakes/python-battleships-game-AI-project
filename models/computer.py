from random import randint, choice
from models.Artificial_intelligence import Smart_ai
from models.ocean import Ocean
from models.ship import Ship


class Computer:
    """
    Constructs a Computer object, def multiple methods for it manipulation, returns it as a formatted string
    """
    allowed_levels = ["easy", "medium", "hard"]
    ships = Ship.sizes

    def __init__(self, level):
        """
        Constructs a Computer object

        Instance Attributes
        -------------------
        self.name
        data: string
            description: name of the player

        self.level
        data: string
            description: Level of computer's logic. May be easy, medium or hard.

        self.ocean
        data: Ocean()
            description: Ocean instance

        self.last_shot
        data: Ocean.board coordinates
            description: Contains coordinates of last computer's shot

        self.previous shot
        data: Ocean.board coordinates
            description: Contains coordinates of previous computer's shot

        last_good_shot
        data: Ocean.board coordinates
            description: Contains coordinates of last good computer's shot

        good_shot
        data: list
            description: List of all computer's good shots
        """

        self.name = "Computer"
        self.level = level.lower()
        self.ocean = Ocean()
        self.last_shot = None
        self.previous_shots = []
        self.is_winner = False
        self.last_good_shot = None
        self.good_shots = []
        self.is_loser = False

    def check_status(self):
        """
        Sets is_loser attribute to True if all player's ships are sunk, otherwise sets False.

        Returns
        -------
        self.is_loser
        """

        self.is_loser = self.ocean.is_every_ship_sunk()

        return self.is_loser

    def shot(self, enemy_ocean):
        """
        Returns enemy Ocean object with one more Square hit

        Parameters
        ---------
        enemey_ocean: :object:
            instance of Ocean()

        Returns
        -------
        self.is_loser
        """

        hit = False
        while not hit:
            if self.level == "easy":
                coordinates = self.random_shot()
                if coordinates == self.last_shot:
                    continue
                enemy_ocean = self.normal_shot(coordinates, enemy_ocean)
            if self.level == "medium":
                if self.last_shot is None:
                    coordinates = self.random_shot()
                    enemy_ocean = self.normal_shot(coordinates, enemy_ocean)
                elif len(self.good_shots) > 0:
                    enemy_ocean = self.near_shots(enemy_ocean)
                elif len(self.good_shots) == 0:
                    enemy_ocean = self.smart_shot_search(enemy_ocean)
            if self.level == "hard":
                ai = Smart_ai(enemy_ocean)
                if self.last_shot is None:
                    coordinates = ai.map()
                    enemy_ocean = self.normal_shot(coordinates, enemy_ocean)
                elif len(self.good_shots) > 0:
                    enemy_ocean = self.near_shots(enemy_ocean)
                elif len(self.good_shots) == 0:
                    enemy_ocean = self.smart_shot_search(enemy_ocean)
            hit = True
            return enemy_ocean

    def set_ships(self):
        """
        Randomly places ships on the Ocean.board.

        Returns
        -------
        enemey_ocean: :object:
            instance of Ocean()
        """

        directions = ['up', 'down', 'left', 'right']

        for name, length in Ship.sizes.items():
            good_ship = True

            while good_ship:
                row = randint(0, 9)
                column = randint(0, 9)
                direction = choice(directions)
                ship = Ship(name, row, column, direction)
                good_ship = ship.check_enviroment(self.ocean.board)
                ship.place_ship(self.ocean.board)
                self.ocean.add_ship_to_ocean(ship)

    def mark_sips(self, enemy_ocean, square):
            """
            Sets correct Square object is_hit attribute to True

            Parameters
            ---------
            enemey_ocean: :object:
                instance of Ocean()

            Returns
            -------
            self.is_loser
            """
            for ship in enemy_ocean.ships:
                for sqr in ship.squares:
                    if sqr == square:
                        sqr.hit()
            for another_ship in self.ocean.ships:
                for sqr1 in another_ship.squares:
                    if sqr1 == square:
                        sqr1.hit()
            return enemy_ocean

    def random_shot(self):
        """
        Return random shot
        -------
        list
        """

        row = randint(0, 9)
        column = randint(0, 9)
        return [row, column]

    def normal_shot(self, coordinates, enemy_ocean):
        """
        Makes shot based on last shots, last good shots etc.

        Parameters
        ---------
        enemey_ocean: :object:
            instance of Ocean()

        coordinates: list

        Returns
        -------
        enemy_object: :obj:
        """

        coordinates = self.check_coordinates(coordinates)
        square = enemy_ocean.board[coordinates[0]][coordinates[1]]
        if not square.is_hit:
            enemy_square = self.ocean.enemy_board[coordinates[0]][coordinates[1]]
            square.hit()
            enemy_ocean = self.mark_sips(enemy_ocean, square)
            if square.is_element_of_ship:
                enemy_square.is_element_of_ship = True
                self.last_good_shot = coordinates
            enemy_square.hit()
            self.last_shot = coordinates
        return enemy_ocean

    def smart_shot_search(self, enemy_ocean):
        """
        Search for the best shot

        Parameters
        ---------
        enemey_ocean: :object:
            instance of Ocean()

        Returns
        -------
        enemy_object: :obj:
        """
        # square = enemy_ocean.board[coordinates[0]][coordinates[1]]

        hit = False
        while not hit:
            coordinates = None
            if self.last_good_shot is not None:
                if self.last_good_shot[0] - 1 >= 0:
                    if not self.ocean.enemy_board[self.last_good_shot[0] - 1][self.last_good_shot[1]].is_hit:
                        coordinates = (self.last_good_shot[0] - 1, self.last_good_shot[1])
                        enemy_ocean = self.normal_shot(coordinates, enemy_ocean)
                        hit = True
                        return enemy_ocean
                elif self.last_good_shot[0] + 1 <= 9:
                    if not self.ocean.enemy_board[self.last_good_shot[0] + 1][self.last_good_shot[1]].is_hit:
                        coordinates = (self.last_good_shot[0] + 1, self.last_good_shot[1])
                        enemy_ocean = self.normal_shot(coordinates, enemy_ocean)
                        hit = True
                        return enemy_ocean

                elif self.last_good_shot[1] + 1 <= 9:
                    if not self.ocean.enemy_board[self.last_good_shot[0]][self.last_good_shot[1] + 1].is_hit:
                        coordinates = (self.last_good_shot[0], self.last_good_shot[1] + 1)
                        enemy_ocean = self.normal_shot(coordinates, enemy_ocean)
                        hit = True
                        return enemy_ocean
                elif self.last_good_shot[1] - 1 >= 0:
                    if not self.ocean.enemy_board[self.last_good_shot[0]][self.last_good_shot[1] - 1].is_hit:
                        coordinates = (self.last_good_shot[0], self.last_good_shot[1] - 1)
                        enemy_ocean = self.normal_shot(coordinates, enemy_ocean)
                        hit = True
                        return enemy_ocean

            for i, row in enumerate(self.ocean.enemy_board):
                for j, column in enumerate(row):
                    if self.ocean.enemy_board[i][j].is_hit and self.ocean.enemy_board[i][j].is_element_of_ship:
                        new_coordinates = False
                        if i + 1 <= 9 and not self.ocean.enemy_board[i + 1][j].is_hit:
                            coordinates = (i + 1, j)
                            new_coordinates = self.check_smart_shot_coordinates(coordinates)
                            if new_coordinates:
                                enemy_ocean = self.normal_shot(coordinates, enemy_ocean)
                                hit = True
                                return enemy_ocean
                        elif i - 1 >= 0 and not self.ocean.enemy_board[i - 1][j].is_hit:
                            coordinates = (i - 1, j)
                            new_coordinates = self.check_smart_shot_coordinates(coordinates)
                            if new_coordinates:
                                enemy_ocean = self.normal_shot(coordinates, enemy_ocean)
                                hit = True
                                return enemy_ocean
                        elif j + 1 <= 9 and not self.ocean.enemy_board[i][j + 1].is_hit:
                            coordinates = (i, j + 1)
                            new_coordinates = self.check_smart_shot_coordinates(coordinates)
                            if new_coordinates:
                                enemy_ocean = self.normal_shot(coordinates, enemy_ocean)
                                hit = True
                                return enemy_ocean
                        elif j - 1 >= 0 and not self.ocean.enemy_board[i][j - 1].is_hit:
                            coordinates = (i, j - 1)
                            new_coordinates = self.check_smart_shot_coordinates(coordinates)
                            if new_coordinates:
                                enemy_ocean = self.normal_shot(coordinates, enemy_ocean)
                                hit = True
                                return enemy_ocean
            if hit is False:
                coordinates = self.random_shot()
                enemy_ocean = self.normal_shot(coordinates, enemy_ocean)
                hit = True
                return enemy_ocean

    def check_coordinates(self, coordinates):
        new_coordinates = False
        while not new_coordinates:
            if coordinates not in self.previous_shots:
                self.previous_shots.append(coordinates)
                new_coordinates = True
            else:
                coordinates = self.random_shot()

        return coordinates

    def check_smart_shot_coordinates(self, coordinates):
        new_coordinates = False
        while not new_coordinates:
            if coordinates not in self.previous_shots:
                new_coordinates = True
        return new_coordinates

    def __str__(self):
        if self.is_loser is True:
            return "{} is a loser!".format(self.name)
        else:
            return "{} has won the game!".format(self.name)

    def near_shots(self, enemy_ocean):
        for good_shot in self.good_shots:
            if good_shot[0] - 1 >= 0 and good_shot[0] + 1 <= 9 and good_shot[1] - 1 >= 0 and good_shot[
               1] + 1 <= 9:
                if not self.ocean.enemy_board[good_shot[0] - 1][good_shot[1]].is_hit:
                    coordinates = (good_shot[0] - 1, good_shot[1])
                    enemy_ocean = self.normal_shot(coordinates, enemy_ocean)
                    hit = True
                    return enemy_ocean
                elif not self.ocean.enemy_board[good_shot[0] + 1][good_shot[1]].is_hit:
                    coordinates = (good_shot[0] + 1, good_shot[1])
                    enemy_ocean = self.normal_shot(coordinates, enemy_ocean)
                    hit = True
                    return enemy_ocean

                elif not self.ocean.enemy_board[good_shot[0]][good_shot[1] + 1].is_hit:
                    coordinates = (good_shot[0], good_shot[1] + 1)
                    enemy_ocean = self.normal_shot(coordinates, enemy_ocean)
                    hit = True
                    return enemy_ocean

                elif good_shot[1] - 1 >= 0:
                    if not self.ocean.enemy_board[good_shot[0]][good_shot[1] - 1].is_hit:
                        coordinates = (good_shot[0], good_shot[1] - 1)
                        enemy_ocean = self.normal_shot(coordinates, enemy_ocean)
                        hit = True
                        return enemy_ocean

    def tactical_shot(self, enemy_ocean):
        for i, row in enumerate(self.ocean.enemy_board):
            for j, column in enumerate(row):
                if not self.ocean.enemy_board[i][j].is_hit:
                    coordinates = (i, j)
                    enemy_ocean = self.normal_shot(coordinates, enemy_ocean)
                    return enemy_ocean