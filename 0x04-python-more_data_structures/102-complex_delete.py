#!/usr/binpython3
""" Deletes keys with a specific value"""


def complex_delete(a_dictionary, value):
    itr = a_dictionary.copy()
    for pair in itr.items():
        if pair[1] == value:
            del a_dictionary[pair[0]]
    return a_dictionary
