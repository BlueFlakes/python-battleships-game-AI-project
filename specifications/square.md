
### ```square.py```
#### This is the file containing a square logic.
## Class Square
#### Instance Attributes

* ```is_hit```
    - data: bool
    - description: element of ship, alive or not
    
* ```is_element_of_ship```
    - data: bool
    - description: is square element of ship

#### Instance Methods
* ##### ```__init__(self)```
  Constructs square, which is element of a ship
    
* ```hit(self)```
  
  change the *is_hit* attribute of square
    
* ```__str__(self)```
  
  return string according to is_hit value(bool)

* ```attach_square_to_ship(self)```
  
  change the *is_element_of_ship* attribute
