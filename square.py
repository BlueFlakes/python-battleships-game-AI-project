import ui


class Square:

    def __init__(self):
        self.is_element_of_ship = False
        self.is_hit = False

    def hit(self):
        self.is_hit = True

    def attach_square_to_ship(self):
        self.is_element_of_ship = True

    def __str__(self):
        if self.is_element_of_ship:
            if not self.is_hit:
                part_of_table = 'o'

            else:
                part_of_table = 'x'

        else:
            if not self.is_hit:
                part_of_table = '~'

            else:
                part_of_table = '.'

        return part_of_table
