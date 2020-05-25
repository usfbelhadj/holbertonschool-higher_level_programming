#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Defines Rectangle module"""
    number_of_instances = 0
    """number_of_instances:int"""
    print_symbol = '#'
    """print_symbol:str"""

    def __init__(self, width=0, height=0):
        """
        Parameters
        ----------
        height: int
            height = height of Rectangle
        width: int
            width of Rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
        Parameters
        ----------
        value: int
            value = new size of width
        raise = verify width
            raise TypeError = width must be an integer
            raise ValueError = width must be >= 0
        """
        if type(value) is not (int):
            raise TypeError("width must be an integer")
        if not value >= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
        Parameters
        ----------
        value: int
            value = new size of height
        raise = verify height
            raise TypeError = height must be an integer
            raise ValueError = height must be >= 0
        """
        if type(value) is not (int):
            raise TypeError("height must be an integer")
        if not value >= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Area = area of Rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Perimeter = perimeter of Rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        """Prints"""
        if self.width == 0 or self.height == 0:
            return ""
        return ((str(self.print_symbol) * self.width + '\n') *
                self.height)[:-1]

    def __repr__(self):
        """representation"""
        return 'Rectangle''({}, {})'.format(self.width, self.height)

    def __del__(self):
        """Delete"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''bigger
        Parameters
        ----------
        rect_1:
                Rectangle1
        rect_2:
                Rectangle2
        Raises:
            TypeError: If rect_1, rect_2 are not instances of Rectangle.
        Returns:
            The Bigger
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
