class Square:
    """
    Constructs Square object, def multiple methods for it manipulation, returns it as a formatted string.
    """

    def __init__(self):
        """
        Constructs Square, which is element of a ship.

        Instance Attributes
        -------------------
        * self.is_hit
            - data: bool
            - description: element of ship, alive or not

        * self.is_element_of_ship
            - data: bool
            - description: is square element of ship
        """

        self.is_element_of_ship = False
        self.is_hit = False

    def hit(self):
        """
        Change the *is_hit* attribute of square

        Returns:
        --------
        None
        """
        self.is_hit = True

    def attach_square_to_ship(self):
        """
        Change the *is_element_of_ship* attribute

        Returns:
        --------
        None
        """
        self.is_element_of_ship = True

    def __str__(self):
        """
        Return string according to is_hit value(bool)

        Returns:
        --------
        part_of_table: string

        """
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
