#!/usr/bin/python3
'''Write a Python script that takes in a URL, sends a request'''
from urllib import request
import sys
if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
