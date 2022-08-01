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

    def my_print(self):
        """ Prints the square with # character """

        if self.__size == 0:
            print()
        else:
            width = '#' * self.__size
            for line in range(self.__size):
                print(width)
