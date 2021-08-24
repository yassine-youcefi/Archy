# Archy

 This is a  python package is created to facilitate calculations in the field of aerospace Mathematics Engineering in particular and mathematics geometry in general
As it can calculate the area of shapes and their perimeter with several types of input

## shapes:

- **Point** : accept arguments : a , b, this class contain ` __init__` and `__repr__` methods.

- **Square** : Square class have 2 types of declaration :

  - init \* args:
    height: height of the rectangle
    width: width

  - init \*\* kwargs:
    points: a, b, c, d

This class contain ` __init__` and `__repr__` and other methods :

- perimetre() : this method calculate Square perimetre.
- surface() : this method calculate Square surface.
- diagonal() : this method calculate Square diagonal.

Example :

```python
from archy import  Point, Square


p1 = Point(1, 30)
p2 = Point(4, 80)
p3 = Point(6, 20)
p4 = Point(8, 10)


### Square ###
S1 = Square(4)
S2 = Square(a=p1, b=p2, c=p3, d=p4)
print(f"Square Side > {S1} \n")
print(f"Square side Diagonal > {S1.diagonal()}\n")
print(f"Square side surface > {S1.surface()}\n")
print(f"Square side perimetre > {S1.perimetre()}\n")

```
