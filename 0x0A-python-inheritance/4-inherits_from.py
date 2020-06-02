#!/usr/bin/python3
'''inherits_from Method'''


def inherits_from(obj, a_class):
    """Return Not Same Class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
