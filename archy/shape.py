

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
        return self.long*self.large

    def perimetre(self):
        return ((2*self.large)+(2*self.long))
