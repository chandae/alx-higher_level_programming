#!/usr/bin/python3
""" Base Class """


class Base():
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """ Constructor """
        if id:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
