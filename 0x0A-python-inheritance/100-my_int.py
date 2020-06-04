#!/usr/bin/python3
'''class MyInt that inherits from int'''


class MyInt(int):

    def __eq__(self, num):
        '''Reverse eq'''
        return int(self) != int(num)

    def __ne__(self, num):
        '''Reverse ne'''
        return int(self) == int(num)
