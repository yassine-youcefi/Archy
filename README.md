# Archy

"Archy" is a Python package designed to simplify complex calculations in the aerospace engineering field, with a particular focus on mathematical geometry. It offers the capability to compute the area and perimeter of various shapes, accommodating multiple input formats for ease of use.

[Archiy](https://pypi.org/project/Archiy/1.0.0/)

[![PyPI version](https://badge.fury.io/py/Archiy.svg)](https://badge.fury.io/py/Archiy)


## shapes:

- **Point** : accept arguments : a , b represented the point coordinates in the orthogonal and homogeneous parameters  
 
 This class contain ` __init__`, `__repr__` and 'distance' methods, where the distance method take a point object as parameter to calculate the distance between the points.

 Example :

```python
p1 = Point(1, 30)
p2 = Point(4, 80)

p1.distance(p2)

```

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

- **Triangle** : Triangle class have 2 types of declaration :

  - init \* args:
      accept 3 params type(int) representing side1, side2, side3

      example:
      ```python
        T = Triangle(5, 2, 3)
      ```
      
  <br/>  
  
  - init \*\* kwargs:
      accept 3 params (a,b,c) type(Point) representing side1, side2, side3

      example:
      ```python
      from archiy import Point, Triangle
      p1 = Point(1, 30)
      p2 = Point(4, 80)
      p3 = Point(6, 20)

      T = Triangle(a=p1, b=p2, c=p3)

      ```
This class contain ` __init__` , `__repr__` and 'perimetre'.

  The perimetre method allow to calculate the triangle perimeter :


  ```python

      from archiy import Triangle
      T = Triangle(1,2,10)
      T1.perimetre() 

```

- **Rectangle** : Rectangle class have 2 types of declaration :
    - init \* args: accept 2 params : (height,width)
        
        example:
        ```python
        from archiy import
        R = Rectangle(5,2)
        ```
    - init \*\* kwargs: accept 4 params (a,b,c,d) type(Point)

        example:
        ```python
        from archiy import Point, Rectangle
        p1 = Point(1, 30)
        p2 = Point(4, 80)
        p3 = Point(6, 20)
        p4 = Point(8, 10)

        ### Rectangle ###
        R = Rectangle(5, 5)
        print(f"Rectangle > {R}")
        print(f"Rectangle Surface > {R.surface()} \n")
        
        ```

