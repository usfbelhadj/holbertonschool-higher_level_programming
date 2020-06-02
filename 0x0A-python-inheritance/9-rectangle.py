#!/usr/bin/python3
'''BaseGeometry Class'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle Class'''

    def __init__(self, width, height):
        '''Constructor'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Returns area'''
        return self.__width * self.__height

    def __str__(self):
        '''Print String'''
        return '[Rectangle]' + str(self.__width) + '/' + str(self.__height)
