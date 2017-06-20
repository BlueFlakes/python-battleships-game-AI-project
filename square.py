import ui


class Square:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.is_element_of_ship = False
        self.is_hit = False

    def hit(self):
        if self.is_element_of_ship:
            self.is_hit = True

        else:
            ui.print_error_message('FAIL')

    def attach_square_to_ship(self):
        self.is_element_of_ship = True

    def __str__(self):
        if self.is_element_of_ship:
            if not self.is_hit:
                part_of_table = 'o'

            else:
                part_of_table = 'x'

        else:
            part_of_table = '~'

        return part_of_table


def main():
    pass

if __name__ == "__main__":
    main()
