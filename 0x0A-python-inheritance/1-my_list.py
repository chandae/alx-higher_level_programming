#!/usr/bin/python3
""" My List Module """


class MyList(list):
    """ MyList Class """

    def print_sorted(self):
        """ Prints list in sorted order """
        print(sorted(self))
