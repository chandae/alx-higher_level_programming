#!/usr/bin/python3
""" Function module that compares two objects """


def is_same_class(obj, a_class):
    """
        Returns True if obj is instance of a_class
    """
    return type(obj) is a_class
