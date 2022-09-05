#!/usr/bin/python3
"""
    Returns a dictionary description with simple data structures
    (list, dictionary, string, integer and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """
        Args:
            obj - instance of a class
        Returns: dictionary
    """
    return obj.__dict__
