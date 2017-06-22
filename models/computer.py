from random import randint, choice

from models.ocean import Ocean
from models.ship import Ship


class Computer:
    allowed_levels = ["Easy", "Medium", "Hard"]

    def __init__(self, level):
        self.name = "Computer"
        self.level = level
        self.ocean = Ocean()
        self.last_shot = []
        self.previous_shots = []
        self.is_winner = False

    def check_status(self):
        for ship in self.ocean.ships:
            ship.ship_status()
        self.is_winner = self.ocean.is_every_ship_sunk()

        return self.is_winner

    def shot(self, enemy_ocean):
        hit = False
        while not hit:
            if self.level == "Easy":
                row = randint(0, 9)
                column = randint(0, 9)
            if [row, column] not in self.previous_shots:
                self.previous_shots.append((row, column))
                square = enemy_ocean.board[row][column]
                if self.last_shot != square:
                    if not square.is_hit:
                        hit = True
                        self.last_shot = enemy_ocean.board[row][column]
                        enemy_square = self.ocean.enemy_board[row][column]
                        square.hit()
                        if square.is_element_of_ship:
                            enemy_square.is_element_of_ship = True
                        enemy_square.hit()
                        return enemy_ocean
                elif square == self.last_shot:
                    continue

    def set_ships(self):
        directions = ['up', 'down', 'left', 'right']

        for name, length in Ship.sizes.items():
            good_ship = True

            while good_ship:
                row = randint(0, 9)
                column = randint(0, 9)
                direction = choice(directions)
                ship = Ship(name, row, column,  direction)
                good_ship = ship.check_enviroment(self.ocean.board)
                ship.place_ship(self.ocean.board)
                self.ocean.add_ship_to_ocean(ship)
