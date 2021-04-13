from archy import Rectangle, Point


p = Point(1, 30)
p2 = Point(4, 80)
p3 = Point(6, 20)
p4 = Point(8, 10)


g = Rectangle(a=p, b=p2, c=p3, d=p4)
print(g.diagonal())
