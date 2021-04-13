
from math import sqrt


class Point():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def distance(self, other):
        try:
            if not isinstance(other, Point):
                raise ValueError('the other must be point')
            distance = sqrt(pow(self.a-other.a, 2) + pow(self.b - other.b, 2))
            return distance

        except ValueError as r:
            print(r)


class Rectangle():

    '''
    init
    long: longeur
    large: large
    '''

    def __init__(self, long, large):
        self.long = long
        self.large = large

    def __repr__(self):
        return 'long : {} , large : {}'.format(self.long, self.large)

    '''
    surface this method calculate a surface of the object
    '''

    def surface(self):
        surface = self.long*self.large
        return surface

    def perimetre(self):
        perimetre = ((2*self.large)+(2*self.long))
        return perimetre

    def diagonal(self):
        diagonal = sqrt(pow(self.long, 2)+pow(self.large, 2))
        return diagonal


class SpaceRectangle():
    def __init__(self, **kwargs):
        self.a = kwargs['a']
        self.b = kwargs['b']
        self.c = kwargs['c']
        self.d = kwargs['d']

    def __repr__(self):
        return 'a : {} , b : {} , c : {} , d : {}'.format(self.a, self.b, self.c, self.d)

    # def surface(self):
