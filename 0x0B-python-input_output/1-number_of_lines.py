#!/usr/bin/python3
'''number_of_lines Function'''


def number_of_lines(filename=""):
    '''number_of_lines: Sum of lines in the file
       filename: Name of the file
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        line_num = 0
        lines = f.readlines()
        for line in range(len(lines)):
            line_num += 1
        return(line_num)
