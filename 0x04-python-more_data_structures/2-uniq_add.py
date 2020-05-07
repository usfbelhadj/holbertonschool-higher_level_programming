#!/usr/bin/python3
def uniq_add(my_list=[]):
    mat = []
    for i in my_list:
        if i not in mat:
            mat.append(i)
    s = 0
    for j in mat:
        s += j
    return s
