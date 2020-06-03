#!/usr/bin/python3
'''write_file Function'''


def write_file(filename="", text=""):
    '''write_file: Write a file
       filename: Name of the file
       text: text to write in the file
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
