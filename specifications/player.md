### `player.py`

This is the file containing a `Player` class logic.

### Class Player

__Instance Attributes__

* `name`
  - data: string
  - description: name of the player

* `is_loser`
  - data: boolean
  - description: Is True if player lose, otherwise is False.

* `ocean`
  - data: Ocean()
  - description: Ocean instance

* `counted_shots`
  - data: int
  - description: Shots used by player

__Instance methods__

* ##### ` __init__(self, name)`

    - Constructs a Player object

* ` __str__(self)`

    - Returns string with information about win or lose of the player, based on attribute *is_loser*.
    
 
* `check_status(self)`

    - Sets *is_loser* attribute to True if all player's ships are sunk, otherwise sets False
    
 
* `shot(self, enemy_ocean)`

    - Takes input with coordinates to shot from player, then checks if player can shot there. 
      If yes, changes *is_hit* attribute of correct square to True.
      If no, asks for coordinates again.
    
 
* `set_ships(self)`

    - Asks player for coordinates to place ships on his ocean, checks if it's possible.
      If yes, places ship on the provided coordinates.
      If no, asks for coordinates again.
    
   

