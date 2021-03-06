#!/usr/bin/python3
""" My square module """


class Square():
    """ Square class """

    def __init__(self, size=0):
        """ Constructor """
        
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def size(self):
        """ Returns the square size """

        return self.__size

    def area(self):
        """ Returns current square area """

        return self.__size ** 2
