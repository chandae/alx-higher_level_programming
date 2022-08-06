#!/usr/bin/python3
""" Check if an object is an instance of a given class """


def inherits_from(obj, a_class):
    """ Check if an object is an instance of given class """
    """
        inherits_from returns true if object is instance of a class
        that inherited directly or indirectly from the specified class.
        Args:
            obj (object): object.
            a_class (class): class.
        Returns: True or False.
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
