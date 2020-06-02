#!/usr/bin/python3
'''inherits_from Method'''


def inherits_from(obj, a_class):
    """Return Not Same Class
    """
    if type(obj) is not a_class:
        return True
    else:
        return False
