from archy import Rectangle, SpaceRectangle, Point
g = SpaceRectangle(a=(1, 3), b=(3, 3), c=(3, 1), d=(1, 1))
print(g)

p = Point(5, 10)
p2 = Point(5, 10)
print(p.distance(p2))
