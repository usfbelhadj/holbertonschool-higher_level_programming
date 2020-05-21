#!/usr/bin/python3
"""Module Square"""


class Square:
    """Defines Square module"""
    def __init__(self, size=0):
        """
        Parameters
        ----------
        size: int
            size = size of square
        """
        self.__size = int(size)
        
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Parameters
        ----------
        value: int
            value = new size of square
        raise = verify size
            raise TypeError = size must be an integer
            raise ValueError = Size Must be Positive
        """
        if type(value) is not int:
            raise TypeError("size must be a number")
        if not value >= 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """
        Area = area of square
            Parameters
            ----------
            size: int
                size = size of square
        """
        return self.__size ** 2
    def __eq__(self, other):
        return self.area() == other.area()
    def __neq__(self, other):
        return self.area() != other.area()
    def __su__(self, other):
        return self.area() < other.area()
    def __inf__(self, other):
        return self.area() > other.area()
    def __eqsu__(self, other):
        return self.area() <= other.area()
    def __eqinf__(self, other):
        return self.area() >= other.area()
