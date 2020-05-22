#!/usr/bin/python3
"""Module add_integer"""


def text_indentation(text):
    """
        Parameters
        ----------
        text: str
    """
    if type(text) is not(str):
        raise TypeError("text must be a string")

    c = ""
    for i in text:
        c += i
        if i in ":.?":
            print(c.lstrip(), end="\n")
            c = ""
    print(text)
    
    
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
