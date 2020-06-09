#!/usr/bin/python3
'''Rectangle Class'''
from models.base import Base


class Rectangle(Base):
    '''Class Rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor'''
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
        '''Function for validating the value'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if bool and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not bool and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        '''area of this rectangle'''
        return self.width * self.height

    def display(self):
        '''representation of this rectangle'''
        if self.y != 0:
            p = self.y - 1
            print('\n' * p)
            for i in range(self.height):
                print((' ' * self.x) + ('#' * self.width), end='')
                print()
        else:
            for i in range(self.height):
                print((' ' * self.x) + ('#' * self.width), end='')
                print()

    def __str__(self):
        '''info about this rectangle'''
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        '''Update with kwargs'''
        attribute_list = ["id", "width", "height", "x", "y"]
        if args is not None:
            for i in range(len(args)):
                if i >= len(attribute_list):
                    break
                setattr(self, attribute_list[i], args[i])
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                if key in attribute_list:
                    setattr(self, key, value)
