#!/usr/bin/python3
""" Base Geometry Module """


class BaseGeometry:
    """ Base Geometry """

    def area(self):
        """ Undefined """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """

        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Rectangle Module """

    def __init__(self, width, height):
        """ Constructor """
        super().__init__()

        if not self.integer_validator("width", width):
            self.__width = width
        if not self.integer_validator("height", height):
            self.__height = height
