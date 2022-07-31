#!/usr/bin/python3
""" Returns a key with the largest integer value """


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if not a_dictionary:
        return None
    new_dict = sorted(a_dictionary.items(), key=lambda pair: pair[1])
    return new_dict[-1][0]
