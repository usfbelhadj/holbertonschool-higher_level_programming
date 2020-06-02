#!/usr/bin/python3
'''BaseGeometry Class'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle Class'''
    def __init__(self, width, height):
        '''Constructor'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def get_width(self):
        '''Getter'''
        return self.__width

    def set_width(self, width):
        '''Setter'''
        self.__width = width

    def get_height(self):
        '''Getter'''
        return self.__height

    def set_height(self, height):
        '''Setter'''
        self.__height = height
