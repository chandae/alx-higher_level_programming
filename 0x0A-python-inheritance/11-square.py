#!/usr/bin/python3
""" Base Geometry Module """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class """

    def __init__(self, size):
        """ Constructor """
        self.integer_validator("size", size)

        self.__size = size

    def __str__(self):
        """ Returns string representation of Square object """
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """ Calculates Square Area """
        return self.__size ** 2
