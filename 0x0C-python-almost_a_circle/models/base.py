#!/usr/bin/python3
""" Base Class """
import json


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

    @staticmethod
    def to_json_string(list_dict):
        """ returns json string representation """
        if list_dict is None or list_dict == {}:
            return "[]"
        return json.dumps(list_dict)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes json string representation of Base/Child instances to file """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
