
from math import sqrt


class Point():

    '''
    Point class :
        points arguments : a , b
    '''

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "({} , {})".format(self.a, self.b)

    def distance(self, other):
        try:
            if not isinstance(other, Point):
                raise ValueError('the other must be point')
            distance = sqrt(pow(self.a-other.a, 2) + pow(self.b - other.b, 2))
            return distance

        except ValueError as r:
            print(r.__class__() + r)


class Rectangle():

    '''

    Rectangle class

    have 2 types of declaration :

    1 - init *args :
        length : length of the rectangle
        width: width

    2 - init **kwargs :
        points : a , b , c , d


    '''

    def __init__(self, *args, **kwargs):

        try:
            if len(args) > 0 and len(kwargs) > 0:
                raise ValueError(
                    'the class can take one type of arguments args or kwargs')

            if len(kwargs) > 0:

                for key, value in kwargs.items():

                    if not isinstance(value, Point):
                        raise ValueError('all params must be points')

                if len(kwargs) < 4:
                    raise KeyError('number of  kwargs must be 4')

                # if kwargs['a']
                self.a = kwargs['a']
                self.b = kwargs['b']
                self.c = kwargs['c']
                self.d = kwargs['d']

                self.length = Point.distance(self.a, self.b)
                self.width = Point.distance(self.b, self.c)

            if len(args) > 0:
                if len(args) < 2:
                    raise KeyError('number of  args must be 2')
                self.length = args[0]
                self.width = args[1]

        except ValueError as r:
            print(r)

    def __repr__(self):
        try:
            return 'a = {} , b = {} , c = {} , d = {} \n  length  : {} , width : {} '.format(self.a, self.b, self.c, self.d, self.length, self.width)
        except:

            return 'length  : {} , width : {}'.format(self.length, self.width)

    '''
    surface this method calculate a surface of the object

    '''

    def surface(self):
        surface = self.length * self.width
        return surface

    def perimetre(self):
        perimetre = ((2*self.width)+(2*self.length))
        return perimetre

    def diagonal(self):
        diagonal = sqrt(pow(self.length, 2)+pow(self.width, 2))
        return diagonal


class Square():
    '''

    Square class
    have 2 types of declaration:

    1 - init * args:
        length: length of the rectangle
        width: width

    2 - init ** kwargs:
        points: a, b, c, d
    '''

    def __init__(self, *args, **kwargs):
        try:
            if len(args) > 0 and len(kwargs) > 0:
                raise ValueError(
                    'the class can take one type of arguments args or kwargs')

            if len(kwargs) > 0:
                for key, value in kwargs.items():

                    if not isinstance(value, Point):
                        raise ValueError('all params must be points')

                if len(kwargs) < 4:
                    raise KeyError('number of  kwargs must be 4')
                self.a = kwargs['a']
                self.b = kwargs['b']
                self.c = kwargs['c']
                self.d = kwargs['d']

                self.side = Point.distance(self.a, self.b)

            if len(args) > 0:
                if len(args) < 1:
                    raise KeyError('number of  args must be 1')
                self.side = args[0]
        except ValueError as r:
            print(r)

    def __repr__(self):
        try:
            return 'a = {} , b = {} , c = {} , d = {} \n  side = {} '.format(self.a, self.b, self.c, self.d, self.side)
        except:

            return 'side  : {}'.format(self.side)

        '''
        surface methode to calculate square surface 
        '''

    def surface(self):
        surface = pow(self.side, 2)
        return surface

        '''
        perimetre methode to calculate square perimetre 
        '''

    def perimetre(self):
        perimetre = self.side * 4
        return perimetre

        '''
         methode to calculate square diagonal 
        '''

    def diagonal(self):
        diagonal = sqrt(pow(self.side, 2)+pow(self.side, 2))
        return diagonal
