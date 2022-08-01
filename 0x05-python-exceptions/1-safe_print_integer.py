#!/usr/bin/python3
""" Prints integer in correct format """


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False