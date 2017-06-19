from square import Square


class Ship:

    def __init__(self, ship_name):
        self.name = ship_name.lower()
        self.is_horizontal = False
        self.is_sunk = False
        self.start_column = ""
        self.start_row = ""

        self.squares_list = self.set_size()

    def set_size(self):
        sizes = {"carrier": 5, "battleship": 4, "cruiser": 3, "submarine": 3, "destroyer": 2}
        size = sizes[self.name]

        return [Square() for i in range(size)]

    def check_status(self):
        is_hit_statuses = [square.is_hit for square in self.squares_list]

        self.is_sunk = False if False in is_hit_statuses else True

    def __str__(self):
        pass
