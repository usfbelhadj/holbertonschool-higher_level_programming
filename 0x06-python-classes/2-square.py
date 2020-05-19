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
        raise = verify size
            raise TypeError = The size Must be Integer
            raise ValueError = Size Must be Positive
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if not size >= 0:
            raise ValueError("size must be >= 0")
        self.__size = size
