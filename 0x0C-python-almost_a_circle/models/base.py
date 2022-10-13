#!/usr/bin/python3
""" Base Class """


class Base():
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """ Constructor """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    def to_json_string(list_dict):
        """ returns json string representation """
        if list_dict is None or list_dict == {}:
            return "[]"
        else:
            return str(list_dict)
