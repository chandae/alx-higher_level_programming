#!/usr/bin/python3
"""
    3-from_json_string: from_json_string()
"""
import json


def from_json_string(my_obj):
    """
        Returns python object from json string

        Args:
            my_obj - object to deserialise
    """
    return json.loads(my_obj)
