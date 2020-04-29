#!/usr/bin/python3
def remove_char_at(str, n):
    lang = len(str)
    if n > lang or n < 0:
        return str
    else:
        for c in str:
            if c != str[n]:
                print(c, end="")
    return ("")
