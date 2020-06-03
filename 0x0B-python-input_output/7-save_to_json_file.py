#!/usr/bin/python3
'''from_json_string Function'''
import json


def save_to_json_file(my_obj, filename):
    '''save_to_json_file: json to a file'''
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(json.dumps(my_obj))
