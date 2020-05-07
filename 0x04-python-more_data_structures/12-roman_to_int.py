#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
    j = 0
    key_list = list(roman_dic.keys())
    val_list = list(roman_dic.values())
    for i in roman_string:
        val = (val_list[key_list.index(i)])
        j = j + val
    return(j)
