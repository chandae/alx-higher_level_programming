#!/usr/bin/python3
"""
    1-write_file: write_file()
"""


def write_file(filename="", text=""):
    """
        Writes a string to a file and
        return the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
