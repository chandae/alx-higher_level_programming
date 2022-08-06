#!/usr/bin/python3
""" Check if an object is an instance of a given class """


def inherits_from(obj, a_class):
    """ Check if an object is an instance of given class """
    status = (isinstance(obj, a_class)) or type(obj) is a_class
    return status
