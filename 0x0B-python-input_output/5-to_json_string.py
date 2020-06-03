#!/usr/bin/python3
'''to_json_string Function'''
import json


def to_json_string(my_obj):
    '''to_json_string : json to string'''
    return json.dumps(my_obj, sort_keys=True)
