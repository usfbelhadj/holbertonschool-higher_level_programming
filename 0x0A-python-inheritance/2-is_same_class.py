#!/usr/bin/python3
'''Mylist Class'''


def is_same_class(obj, a_class):
    """Return object if exactly an instance of the specified class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
