#!/usr/bin/python3
"""
    5-text_indentation: text_indentation()
"""


def text_indentation(text):
    """
        Prints text file with two newlines after
        each one of these characters: . ? :

        Args:
            text: first argument (text to print)
        Returns:
            None
    """

    if text is None or not (isinstance(text, str)):
        raise TypeError("text must be a string")
    elif not text.strip():
        pass
    else:
        line = ""
        for char in text:
            if char not in ".?:":
                line += char
            else:
                line += char
                print(line.strip())
                print()
                line = ""
        if line:
            print(line.strip(), end="")
