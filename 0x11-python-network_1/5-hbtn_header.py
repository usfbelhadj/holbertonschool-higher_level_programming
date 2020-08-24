#!/usr/bin/python3
'''Write a Python script that takes in a URL, sends a request'''
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
