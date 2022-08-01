#!/usr/bin/python3
""" My Square Module """


class Square():
    """ Square class """

    def __init__(self, size=0):
        """ Constructor """

        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """ Returns the square size """

        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method for private attribute size """

        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns current square area """

        return self.__size ** 2

    def __eq__(self, other) -> bool:
        """ Magic method for equality operator """

        return self.area() == other.area()

    def __ne__(self, other):
        """ Magic method for not equal to operator """

        return self.area() != other.area()

    def __lt__(self, other):
        """ Magic method for less than operator """

        return self.area() < other.area()

    def __gt__(self, other):
        """ Magic method for greater than operator """

        return self.area() > other.area()

    def __le__(self, other):
        """ Magic method for less than or equal to operator """

        return self.area() <= other.area()

    def __ge__(self, other):
        """ Magic method for greater than or equal to operator """

        return self.area() >= other.area()
