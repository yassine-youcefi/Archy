from archy import Rectangle, Point, Square, Triangle


p1 = Point(1, 30)
p2 = Point(4, 80)
p3 = Point(6, 20)
p4 = Point(8, 10)


# R = Rectangle(5, 5)
# print(R.surface())

# S = Square(4)
# print(S.diagonal())

T = Triangle(a=p1, b=p2, c=p3)
print(T)
