#!/usr/bin/python3
"""
    5-save_to_json_file: save_to_json_file()
"""
import json


def save_to_json_file(my_obj, filename):
    """
        Writes and saves json object to a text file

        Args:
            my_obj -  object to write to text file
            filename -  name of file to write to
    """
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(my_obj, json_file)
