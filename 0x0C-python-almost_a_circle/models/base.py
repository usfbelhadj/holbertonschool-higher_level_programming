#!usr/bin/python3
'''Base Class'''


class Base:
    '''Class Bbase'''
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if not self.id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        if self.id:
            Base.__nb_objects
