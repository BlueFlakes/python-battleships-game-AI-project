### `computer.py`

This is the file containing a `Computer` class logic.

### Class Player

__Instance Attributes__

* `name`
  - data: string
  - description: name of the player

* `level`
  - data: string
  - description: Level of computer's logic. May be easy, medium or hard.

* `ocean`
  - data: Ocean()
  - description: Ocean instance

* `last_shot`
  - data: Ocean.board coordinates
  - description: Contains coordinates of last computer's shot
  
* `previous shot`
  - data: Ocean.board coordinates
  - description: Contains coordinates of previous computer's shot

* `last_good_shot`
  - data: Ocean.board coordinates
  - description: Contains coordinates of last good computer's shot

* `good_shots`
  - data: list
  - description: List of all computer's good shots

__Instance methods__

* ##### ` __init__(self, name)`

    - Constructs a Computer object

* ` __str__(self)`

    - Returns string with information about win or lose of the player, based on attribute *is_loser*.
    
 
* `check_status(self)`

    - Sets *is_loser* attribute to True if all player's ships are sunk, otherwise sets False

* `shot(self, enemy_ocean)`

    - Returns enemy *Ocean* object with one more *Square* hit
    
 
* `set_ships(self)`

    - Randomly places ships on the *Ocean.board*

* `mark_sips(self, enemy_ocean, square)`

    - Sets correct *Square* object *is_hit* attribute to True

* `random_shot(self)`

    - Returns two numbers randomly drawed between 0 and 9.
    
 
* `normal_shot(self, coordinates, enemy_ocean)`

    - Makes shot based on last shots, last good shots etc.
 
