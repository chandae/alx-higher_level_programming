#!/usr/bin/python3
"""
    Loads script arguments to list and then saves list to json file
"""
import json
import sys


def load_from_json_file(filename):
    """
        Creates python oject from json file

        Args:
            filename -  name of file to get object from
    """
    with open(filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def save_to_json_file(my_obj, filename):
    """
        Writes and saves json object to a text file

        Args:
            my_obj -  object to write to text file
            filename -  name of file to write to
    """
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(my_obj, json_file)


if __name__ == "__main__":

    filename = "add_item.json"

    try:
        arg_list = load_from_json_file(filename)
    except Exception as err:
        arg_list = []

    for arg in sys.argv[1:]:
        arg_list.append(arg)
    save_to_json_file(arg_list, filename)
