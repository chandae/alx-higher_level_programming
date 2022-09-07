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
        """ Width getter and setter property """
        return self.width

    @width.setter
    def width(self, value):
        """ Width public setter method """
        self.width = value

    @width.getter
    def width(self):
        """ Width public getter method """
        return self.width

    @property
    def height(self):
        """ Height getter and setter property """
        return self.height

    @height.setter
    def height(self, value):
        """ Height public setter method """
        self.height = value

    @height.getter
    def height(self):
        """ Height public getter method """
        return self.height

    @property
    def x(self):
        """ x getter and setter property """
        return self.x

    @x.setter
    def x(self, value):
        """ x public setter method """
        self.x = value

    @x.getter
    def x(self):
        """ x public getter method """
        return self.x

    @property
    def y(self):
        """ y getter and setter property """
        return self.y

    @y.setter
    def y(self, value):
        """ y public setter method """
        self.y = value

    @y.getter
    def y(self, value):
        """ y public getter method """
        return self.y
