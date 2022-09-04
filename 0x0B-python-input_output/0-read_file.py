#!/usr/bin/python3
"""
    0-read_file: read_file()
"""


def read_file(filename=""):
    """ Reads text file (utf-8) and outputs contents to stdout """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
