#!/usr/bin/python3
""" MyInt Module """


class MyInt(int):
    """ Int Child Class """

    def __eq__(self, __x) -> bool:
        """ Inverts == comparison """
        return not self.__int__() == __x

    def __ne__(self, __x) -> bool:
        return not self.__int__() != __x
