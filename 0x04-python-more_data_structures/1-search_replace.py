#!/usr/bin/python3
""" Function replaces all occurences of an element by another in a new list """


def search_replace(my_list, search, replace):
    array = my_list.copy()
    for index, element in enumerate(array):
        if element == search:
            array[index] = replace
    return array
