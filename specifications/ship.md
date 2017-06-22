### `ship.py`

This is the file containing a `SHIP` item logic.

### Class Ship

__Instance Attributes__

* `squares`
  - data: list
  - description: list of square() objects

* `name`
  - data: string
  - description: type of ship, i. e. carrier, cruiser

* `size`
  - data: integer
  - description: lenght of size list

* `direction`
  - data: string
  - description: contains string with direction of ship: "up", "down, "left", "right"
  
* `is_sunk`
  - data: boolean
  - description: contains True if all squares elements are hit, otherwise contains False

* `start_column`
  - data: integer
  - description: one of coordinates which decide where ship will be placed

* `start_row`
  - data: integer
  - description: one of coordinates which decide where ship will be placed

__Instance methods__

* ##### ` __init__(self, name)`

    - Constructs a Ship object
  
*  `check_status(self)`
   - Checks if all squares of ship are hit. If yes, sets *self.is_sunk* to True.

*  `set_size(self)`
   - Sets *size* attribute based on name of ship.
   
*  `place_ship(self, board)`
   - Changes correct square's *is_element_of_ship* attribute to True

*  `check_enviroment(self, board)`
   - Returns True if there is another ship close to the new ship position, else returns False

*  `set_squares_around(self, board, end_row, end_column)`
   - Returns list of *Square* objects which are around ship's position

*  `set_ship_end(self, board)`
   - Returns end row and end column of ship
