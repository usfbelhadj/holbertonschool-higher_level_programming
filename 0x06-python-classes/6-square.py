class Square:
    """Module Square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Parameters
        ----------
        size: int
            size = size of square
        position: int
            position of the square
        """
        self.__size = size
        self.__position = position
        if not position[1] > 0:
            print()

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
            raise TypeError("size must be an integer")
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

    def my_print(self):
        """Prints"""
        if (self.__size) == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self.__size

    @position.setter
    def position(self, value):
        """
        Parameters
        ----------
        value: int
            value = new size of square
        Raises:
            TypeError: If value is not tuple of 2 positive integers.
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
