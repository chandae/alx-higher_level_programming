#!/usr/bin/python3
""" Adds all unique integers in a list (only once for each integer) """


def uniq_add(my_list=[]):
    new_list = set(my_list.copy())
    return sum(new_list)
