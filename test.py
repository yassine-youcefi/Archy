from archy import Rectangle, Point, Square, Triangle, Plot


p1 = Point(1, 30)
p2 = Point(4, 80)
p3 = Point(6, 20)
p4 = Point(8, 10)

### Point ###
# p1.__repr__()
# p1.x()
# p1.y()
# p1.list()

# ### Rectangle ###
# R = Rectangle(5, 5)
# print(f"Rectangle > {R}")
# print(f"Rectangle Surface > {R.surface()} \n")

# ### Square ###
# S1 = Square(4)
# S2 = Square(a=p1, b=p2, c=p3, d=p4)
# print(f"Square Side > {S1} \n")
# print(f"Square side Diagonal > {S1.diagonal()}\n")
# print(f"Square side surface > {S1.surface()}\n")
# print(f"Square side perimetre > {S1.perimetre()}\n")

# print('-------------------------\n')
# print(f"Square point > {S2} \n")
# print(f"Square pont diagonal > {S2.diagonal()}\n")
# print(f"Square side surface > {S2.surface()}\n")
# print(f"Square side perimetre > {S2.perimetre()}\n")

# ### Triangle ###
# T1 = Triangle(a=p1, b=p2, c=p3)
# T2 = Triangle(5, 2, 3)
# print(f"Triangle with point params > {T1}\n")
# print(f"Triangle with point perimetre > {T1.perimetre()}\n")

# print(f"Triangle with side params > {T2}\n")
# print(f"Triangle with side perimetre > {T2.perimetre()}\n")



### plot ###
print('plot -- ')
# p1.plot(color = 'red')
p = Plot(p1, p2, p3, p4)
# p.__repr__()
# plot points
# p.plot_points()
# p.plot_points_line()

P = Plot()
T = Triangle(a=p1, b=p2, c=p4)
# S = Square(a=p1, b=p2, c=p3, d=p4)
# p.plot_square(S)
p.plot_triangle(T)



# add plot rectangle

