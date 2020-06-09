#!/usr/bin/python3
'''square Class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class Square'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor'''
        super().__init__(size, size, x, y, id=None)

    def __str__(self):
        return ("[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.validation("width", value, False)
        self.width = value
        self.heigth = value