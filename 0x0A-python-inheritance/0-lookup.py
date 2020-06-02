#!/usr/bin/python3
def lookup(obj):
    """lookup:
        F  unction that returns the list of available attributes and methods of an object
    Arguments:
        obj {list} -- [Object to a list]
    """
    return dir(obj)
