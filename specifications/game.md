### `game.py`

This is the file containing a `Game` class logic.

### Class Game

__Instance Attributes__

* `type`
  - data: string
  - description: Contains information about type of game: singleplayer, multiplayer, simulation.

* `player1`
  - data: Player object
  - description: Contains first player object

* `player2`
  - data: Player object
  - description: Contains first player object

* `is_over`
  - data: boolean
  - description: Contains True if one of the players wins, otherwise contains False.
  
* `player_in_round`
  - data: Player object
  - description: Contains Player object which is currently shooting

__Instance methods__

* ##### ` __init__(self, name)`

    - Constructs a Game object

* ` is_game_over(self)`

    - Returns True if someone wins, otherwise returns False
    
 
* `start_game(self)`

    - Calls *set_ships* function for both players, and draws which one will shot first.
    
 
* `player_switch(self)`

    - Switches *player_in_round* attribute from one player to another
    
 
* `turn(self)`

    - Contains whole game loop, which ends when *is_over* attribute is True

* `check_coordinates(cls, coordinates, alphanumeric_dict)`

    - Returns True if player choose a letter between A and J, otherwise returns False.
    
 
* `add_player_to_highscore(self)`

    - At the end of the game, if one of the player's was a *Player* object and he won, saves data about him to .csv file.

