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
        self.__size = size

    def area(self):
        """
        Area = area of square
            Parameters
            ----------
            size: int
                size = size of square
        """
        return self.__size ** 2

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
            raise TypeError = The size Must be Integer
            raise ValueError = Size Must be Positive
        """
        if type(value) is not int:
            raise TypeError("The size Must be Integer")
        if not value >= 0:
            raise ValueError("size must be >= 0")
        self.__size = value
