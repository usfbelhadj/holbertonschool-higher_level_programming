#!/usr/bin/python3
'''Mylist Class'''


class MyList(list):
    """Class Mylist
    """
    def print_sorted(self):
        """Method That Print a sorted List
        """
        print(sorted(self))
