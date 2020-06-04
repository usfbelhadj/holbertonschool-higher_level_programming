#!/usr/bin/python3
'''MyInt Class'''


class MyInt(int):

    def __eq__(self, num):
        '''Reverse eq'''
        return int(self) != int(num)

    def __ne__(self, num):
        '''Reverse ne'''
        return not int(self) != int(num)
