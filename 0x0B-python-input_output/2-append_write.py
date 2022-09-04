#!/usr/bin/python3
"""
    1-append_write: append_write()
"""


def append_write(filename="", text=""):
    """
        Appends a string at the end of a file and
        return the number of characters appended.

        Args:
            filename - name of file to write to
            text - text to be written to flle
        Returns:
            Number of characters appended to file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
