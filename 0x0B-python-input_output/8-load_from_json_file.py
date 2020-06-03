#!/usr/bin/python3
'''load_from_json_file Function'''
import json


def load_from_json_file(filename):
    '''load_from_json_file: read from json file'''
    with open(filename, 'r', encoding='utf-8') as f:
        json_value = f.read()
        return json.loads(json_value)
