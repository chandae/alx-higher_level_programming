#!/usr/bin/python3
"""
    4-print_square: print_square(size)
"""


def print_square(size):
    """
        Prints a square of size <size> and character #

        Args:
            size: first argument (length of the square)
        Returns:
            None (Output is printed)
    """

    if not (isinstance(size, int)):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")
    elif (isinstance(size, float)) and size < 0:
        raise TypeError("size must be an integer")

    # Print the square of size <size>
    for _ in range(size):
        print("#" * size)
