#!/usr/bin/python3
""" script fetches X-User-Id from url passed as argument """
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    
    with urllib.request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
