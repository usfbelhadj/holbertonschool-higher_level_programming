#!/usr/bin/python3
s = ''
for i in range(65, 91):
    if i % 2 == 0:
        i = chr(i + 32)
    else:
        i = chr(i)
    s = i + s
print("{}".format(s), end="")