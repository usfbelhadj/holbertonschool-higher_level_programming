#!/usr/bin/python3
"""Module add_integer"""


def say_my_name(first_name, last_name=""):
    """
        Parameters
        ----------
        first_name: string
        last_name: string
    """
    if type(first_name) is not (str):
        raise TypeError("first_name must be a string")
    if type(last_name) is not (str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
