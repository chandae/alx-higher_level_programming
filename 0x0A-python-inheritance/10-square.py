#!/usr/bin/python3
""" Base Geometry Module """


Rectangle = __import__('9-rectangle').Rectangle


class Sqaure(Rectangle):
    """ Square Class """

    def __init__(self, size):
        """ Constructor """
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """ Calculates Rectangle Area """
        return self.__size ** 2
