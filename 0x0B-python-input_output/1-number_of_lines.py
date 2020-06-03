#!/usr/bin/python3
'''read_file Function'''


def number_of_lines(filename=""):
    with open(filename, 'r', encoding='utf-8') as f:
        line_num = 0
        lines = f.readlines()
        for line in lines:
            line_num += 1
        return line_num
