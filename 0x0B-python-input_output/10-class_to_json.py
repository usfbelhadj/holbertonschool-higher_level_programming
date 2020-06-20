#!/usr/bin/python3
'''from_Class_to_Json Function'''
import json


def class_to_json(obj):
    return obj.__dict__
