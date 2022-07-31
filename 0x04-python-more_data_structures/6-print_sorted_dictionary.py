#!/usr/bin/python3
""" Prints sorted dictionary keys and their values """


def print_sorted_dictionary(a_dictionary):
    for pair in sorted(a_dictionary.items(), key=lambda pair: pair[0]):
        print("{}: {}".format(pair[0], pair[1]))
