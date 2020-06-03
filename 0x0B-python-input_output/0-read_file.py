#!/usr/bin/python3
'''read_file Function'''


def read_file(filename=""):
    '''read_file: Reading File
       filename: Name of the file
    '''
    with open(filename, 'r') as f:
        print(f.read())
