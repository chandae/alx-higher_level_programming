#!/usr/bin/python3
""" Function adds new attribute to object if its possible """


def add_attribute(obj, attr, val):
    """ Attempts to add new attribute to an object """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
