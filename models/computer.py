from random import randint, choice
from models.ship import Ship
from models.ocean import Ocean


class Computer:
    def __init__(self, level):
        self.name = "Computer"
        self.level = level
        self.ocean = Ocean()
        self.last_shot = []

    def check_status(self):
        ships_statuses = [ship.is_sunk for ship in self.ocean.ships]

        self.is_winner = False if False in ships_statuses else True

    def shot(self):
        hit = False
        while not hit:
            row = randint(0, 9)
            column = randint(0, 9)
            square = self.ocean.enemy_board[row][column]
            if self.last_shot != square:
                if not square.is_hit:
                    hit = True
                    square.hit()
                    self.last_shot = self.ocean.enemy_board[row][column]
            elif square == self.last_shot:
                continue

    def set_ships(self):
        directions = ['up', 'down', 'left', 'right']

        for key, value in Ship.sizes.items():
            good_statek = False

            while not good_statek:
                row = randint(0, 9)
                column = randint(0, 9)
                direction = choice(directions)
                ship = Ship(key, row, column,  direction)
                good_statek = ship.check_enviroment(self.ocean.board)

            ship.place_ship(self.ocean.board)
            self.ocean.add_ship_to_ocean(ship)
