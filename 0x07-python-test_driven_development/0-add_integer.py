#!/usr/bin/python3
"""
    0-add_integer: add_integer - returns sum of two integers
"""


def add_integer(a, b=98):
    """
        Returns the sum of two integers

        Args:
            a: first argument
            b: second argument
        Returns:
            The sum of two integers
    """
    if not isinstance(a, int) and not isinstance(a, float) or a is None:
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float) or b is None:
        raise TypeError('b must be an integer')
    if (isinstance(a, float)):
        a = int(a)
    if (isinstance(b, float)):
        b = int(b)

    return a + b
