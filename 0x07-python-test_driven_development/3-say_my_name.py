#!/usr/bin/python3
"""
    3-say_my_name: say_my_name(first_name, last_name="")
"""


def say_my_name(first_name, last_name=""):
    """
        Prints 'My name is <first_name> <last_name>

        Args:
            first_name: first argument
            last_name: second argument (positional)
        Returns:
            None
    """

    if not (isinstance(first_name, str)) or not first_name:
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
