#!/usr/bin/python3
"""
    Loads script arguments to list and then saves list to json file
"""
import json
import os
import sys


def load_from_json_file(filename):
    """
        Creates python oject from json file

        Args:
            filename -  name of file to get object from
    """
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    else:
        with open(filename, 'w', encoding='utf-8') as json_file:
            save_to_json_file([], filename)


def save_to_json_file(my_obj, filename):
    """
        Writes and saves json object to a text file

        Args:
            my_obj -  object to write to text file
            filename -  name of file to write to
    """
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(my_obj, json_file)


if __name__ == '__main__':
    items = load_from_json_file('add_item.json')
    if not items:
        items = load_from_json_file('add_item.json')
    if len(sys.argv) > 1:
        items.extend(sys.argv[1:])
        save_to_json_file(items, 'add_item.json')
