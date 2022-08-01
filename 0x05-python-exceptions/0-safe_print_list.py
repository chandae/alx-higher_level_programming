#!/usr/bin/python3
""" Prints x elements of a list"""


def safe_print_list(my_list=[], x=0):
    try:
        if x <= len(my_list):
            print(*my_list[:x], sep='')
            return x
        else:
            print(*my_list[:x], sep='')
            return len(my_list)
    except IndexError:
        pass
