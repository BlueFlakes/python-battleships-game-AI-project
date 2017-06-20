from ocean import Ocean


class Computer:
    def __init__(self, level):
        self.level = level
        self.ocean = Ocean()

    def check_status(self):
        ships_statuses = [ship.is_sunk for ship in self.ocean.ships]

        self.is_winner = False if False in ships_statuses else True
