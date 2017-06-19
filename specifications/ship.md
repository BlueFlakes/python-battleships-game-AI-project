### `ship.py`

This is the file containing a `SHIP` item logic.

### Class Ship

__Instance Attributes__

* `squares`
  - data: list
  - description: list of square() objects

* `size`
  - data: integer
  - description: lenght of size list

* `is_horizontal`
  - data: boolean
  - description: contains True if ship is placed horizontal, otherwise contains False
  
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

  Constructs a Ship object

* `__str__(self)`

  Returns a formatted string with squares printed horizontally or vertically.
  
*  `check_status(self)`

  Checks if all squares of ship are hit. If yes, sets self.is_sunk to True.

*  `set_size(self)`

  Sets size attribute based on name of ship.
