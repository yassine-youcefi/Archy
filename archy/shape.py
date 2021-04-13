
from math import sqrt


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
