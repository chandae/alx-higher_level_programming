#!/usr/bin/python3
""" Returns the opposite of intersection (difference of sets) """


def only_diff_elements(set_1, set_2):
    return (set_1 - set_2) | (set_2 - set_1)
