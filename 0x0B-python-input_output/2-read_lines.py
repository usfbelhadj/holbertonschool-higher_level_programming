#!/usr/bin/python3
'''read_lines Function'''


def read_lines(filename="", nb_lines=0):
    '''read_lines: Reading lines
       filename: Name of the file
       nb_lines: Number Of The Line
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
        else:
            for line in range(nb_lines):
                print(f.readline(), end='')
