
### ```square.py```
#### This is the file containing a square logic.
## Class Square
#### Instance Attributes
* ```row```
    - data: int
    - description: square horizontal position

* ```column```
    - data: int
    - description: square vertical position

* ```is_hit```
    - data: bool
    - description: element of ship, alive or not

#### Instance Methods
* ##### ```__init__(self, row, column, is_hit)```
    - Constructs an square, element of ship
    
* ```is_hit```
    - change the status of square
    
* ```__str__(self)```
    - return string according to is_hit value(bool)
