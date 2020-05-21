#!/usr/bin/python3
"""Module Square"""
import math


class MagicClass:
    """Defines Square module"""
    def __init__(self, radius=0):
        """
        Parameters
        ----------
        radius: int
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Area = area of square
            Parameters
            ----------
            size: int
                size = size of square
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
