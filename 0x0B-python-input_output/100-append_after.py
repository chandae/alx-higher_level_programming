#!/usr/bin/python3
"""
    Inserts a line of text to a file
    After each line containing a specific string
"""


def append_after(filename="", search="", new=""):
    """
        Appends a line of text to file

        Parameters:
            - filename: name of the file to append text to
            - search: string to look for in the file
            - new: line of text to append to file
    """
    with open(filename, 'r', encoding='UTF-8') as f:
        contents = f.readlines()
        for idx, line in enumerate(contents):
            if search in line.strip():
                contents.insert(idx + 1, new)
    with open(filename, 'w', encoding='UTF-8') as f:
        f.writelines(contents)
