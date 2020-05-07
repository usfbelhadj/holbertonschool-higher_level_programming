#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        key_list = list(a_dictionary.keys())
        val_list = list(a_dictionary.values())
        val = max(val_list)
        for k in a_dictionary.values():
            if val == k:
                return(key_list[val_list.index(k)])
