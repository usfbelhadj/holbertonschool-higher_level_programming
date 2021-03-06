#!/usr/bin/python3
'''sends a POST request to the passed URL'''
import requests
from sys import argv
if __name__ == "__main__":
    response = requests.post(argv[1], data={'email': argv[2]})
    print(response.text)
