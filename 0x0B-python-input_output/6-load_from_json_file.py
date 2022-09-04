#!/usr/bin/python3
"""
    6-load_from_json_file: load_from_json_file()
"""
import json


def load_from_json_file(filename):
    """
        Creates python oject from json file

        Args:
            filename -  name of file to get object from
    """
    with open(filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)
