#!/usr/bin/python3
'''Rectangle Class'''
from models.base import Base


class Rectangle(Base):
    '''Class Rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validation("width", value, False)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validation('height', value, False)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validation('x', value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validation('y', value)
        self.__y = value

    def validation(self, name, value, bool=True):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if bool and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not bool and value <= 0:
            raise ValueError("{} must be > 0".format(name))
