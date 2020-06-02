#!/usr/bin/python3
'''Rectangle Class'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square Class'''

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        
    def area(self):
        '''Returns area'''
        return self.__size* self.__size

    def __str__(self):
        '''Print String'''
        return '[Rectangle] ' + str(self.__size) + '/' + str(self.__size)
