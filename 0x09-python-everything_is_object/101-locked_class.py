#!/usr/bin/python3
""" LockedClass: No new instance attributes permitted """


class LockedClass:
    """ Base Class: No new instance attributes permitted """
    __slots__ = ['first_name']
