#!/usr/bin/python3
""" Base Geometry Module """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle Module """

    def __init__(self, width, height):
        """ Constructor """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def __str__(self):
        """ Returns string representation of Rectangle """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """ Calculates Rectangle Area """
        return self.__width * self.__height
