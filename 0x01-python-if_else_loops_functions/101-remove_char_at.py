#!/usr/bin/python3
def remove_char_at(str, n):
    l = len(str)
    if n > l or n < 0:
        return str
    else:
        for c in str:
            if c != str[n]:
                print(c, end="")
    return ("")
