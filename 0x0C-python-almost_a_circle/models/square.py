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

    def update(self, *args, **kwargs):
        '''Update with kwargs'''
        attribute_list = ["id", "size", "x", "y"]
        if args is not None:
            for i in range(len(args)):
                if i >= len(attribute_list):
                    break
                setattr(self, attribute_list[i], args[i])
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                if key in attribute_list:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''return dictionary'''
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
