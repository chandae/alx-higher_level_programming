#!/usr/bin/python3
""" My Square Module """


class Square():
    """ Square class """

    error_msg = "position must be a tuple of 2 positive integers"

    def __init__(self, size=0, position=(0, 0)):
        """ Constructor """

        # Set private instance attribute size
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        # Set private instance attribute position
        if (isinstance(position, tuple)) and len(position) == 2:
            if isinstance(position[0], int) and isinstance(position[1], int):
                if position[0] >= 0 and position[1] >= 0:
                    self.__position = position
                else:
                    raise TypeError(Square.error_msg)
            else:
                raise TypeError(Square.error_msg)
        else:
            raise TypeError(Square.error_msg)

    def __str__(self):
        """ Prints the square instance with # character """

        if self.__size == 0:
            print()
        else:
            x_position = self.__position[0]
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print("{}{}".format(" " * x_position, "#" * self.__size))
        return ''

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

    @property
    def position(self):
        """ Returns the square position """

        return self.__position

    @position.setter
    def position(self, value):
        """ Setter method for private attribute position """

        if (isinstance(value, tuple)) and len(value) == 2:
            if (isinstance(value[0], int) and isinstance(value[1], int)):
                self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Returns current square area """

        return self.__size ** 2

    def my_print(self):
        """ Prints the square with # character """

        if self.__size == 0:
            print()
        else:
            x_position = self.__position[0]
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print("{}{}".format(" " * x_position, "#" * self.__size))
