#!/usr/bin/python3
""" Multiplies each dict value by 2 """


def multiply_by_2(a_dictionary):
    new_dictionary = dict()
    for key, value in a_dictionary.items():
        new_dictionary[key] = value * 2
    return new_dictionary
