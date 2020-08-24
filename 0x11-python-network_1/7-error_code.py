#!/usr/bin/python3
""" Uses requests module. Prints error code"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    if response.status_code <= 400:
        print(response.text)
    else:
        print("Error code:", response.status_code)
