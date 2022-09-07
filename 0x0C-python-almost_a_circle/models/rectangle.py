#!/usr/bin/python3
""" Base Class Child Class: Rectangle Class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        """ Constructor """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Width getter method """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width public setter method """
        self.valid()
        self.__width = value

    @property
    def height(self):
        """ Height getter method """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height public setter method """
        self.valid()
        self.__height = value

    @property
    def x(self):
        """ x getter method """
        return self.__x

    @x.setter
    def x(self, value):
        """ x public setter method """
        self.valid()
        self.__x = value

    @property
    def y(self):
        """ y getter method """
        return self.__y

    @y.setter
    def y(self, value):
        """ y public setter method """
        self.valid()
        self.__y = value

    def valid(self, name, value, greater_equal=False):
        """ Check if input is an integer """
        if not (isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if not greater_equal:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
