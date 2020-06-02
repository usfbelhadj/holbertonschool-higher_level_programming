#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Return Not Same Class
    """
    if type(obj) == a_class:
        return False
    else:
        return True
