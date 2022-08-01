#!/usr/bin/python3
""" Function prints the first x integer elements of a list """


def safe_print_list_integers(my_list=[], x=0):
    this_list = list(filter(lambda item: str(item).isdigit(), my_list))
    count = 0
    try:
        for i in range(x):
            print("{:d}".format(this_list[i]), end='')
            count += 1
        print()
        return x
    except IndexError:
        print()
        return count
