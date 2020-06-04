#!/usr/bin/python3
'''add_item.json Function'''
import json
import sys
import os


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
filename = 'add_item.json'
open(filename, "a")
try:
    myobj = load_from_json_file("add_item.json")
except ValueError:
    myobj = []
save_to_json_file(myobj + sys.argv[1:], "add_item.json")
