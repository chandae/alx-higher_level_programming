#!/usr/bin/python3
"""
    3-to_json_string: to_json_string()
"""
import json


def to_json_string(my_obj):
    """
        Returns json representation of object(string)

        Args:
            my_obj - object to serialise
    """
    return json.dumps(my_obj)
