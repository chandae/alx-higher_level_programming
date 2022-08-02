#!/usr/bin/python3
""" My Rectangle Module: Python Classes """


class Rectangle():
    """ Base Rectangle Class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Class Constructor: Rectangle Module """

        # Initialise rectangle width
        if not (isinstance(width, int)):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        # Initialise rectangle height
        if not (isinstance(height, int)):
            raise TypeError("height must be an integer")
        elif (height < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

        Rectangle.number_of_instances += 1

    def __str__(self):
        """ Returns string representation of rectangle """

        if (self.__width == 0 or self.__height == 0):
            return ""
        else:
            rect = ""
            for line in range(self.__height):
                rect += self.__width * str(self.print_symbol) + '\n'
            return rect.rstrip()

    def __repr__(self):
        """
        Returns rectangle string representation
        result can be used with eval() to recreate new Rectangle object
        """
        s = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return s

    def __del__(self):
        """"
        Notifies user an rectangle instance is deleted
        Modify number instances accordingly
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """ Instance method returns rectangle width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for attribute width """

        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Instance method returns rectangle height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for attribute height """

        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns rectangle perimeter """
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return 2 * (self.__width + self.__height)
