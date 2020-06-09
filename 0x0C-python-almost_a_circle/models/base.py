#!usr/bin/python3
'''Base Class'''


class Base:
    '''Class Bbase'''
    __nb_objects = 0

    def __init__(self, id=None):
        if not self.id:
            self.id = id
        if self.id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
