#!/usr/bin/python3
"""
    1-write_file: write_file()
"""


def write_file(filename="", text=""):
    """
        Writes a string to a file and
        return the number of characters written

        Args:
            filename - name of file to write to
            text - text to be written to flle
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
