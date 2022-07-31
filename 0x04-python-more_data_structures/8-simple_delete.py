#!/usr/bin/python3
""" Deletes a dictionary key if it exists, else it stays the same """


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
