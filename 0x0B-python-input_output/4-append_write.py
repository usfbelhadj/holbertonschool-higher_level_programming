#!/usr/bin/python3
'''append_write Function'''


def append_write(filename="", text=""):
    '''append_write: Append a file
       filename: Name of the file
       text: text to append in the file
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
