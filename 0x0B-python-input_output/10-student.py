#!/usr/bin/python3
"""
    Student Class: Student
"""


class Student():
    """
        Student Class

        Attributes:
            - first_name: string
            - last_name: string
            - age: integer
    """
    def __init__(self, first_name, last_name, age) -> None:
        """ Constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None) -> dict:
        """ Returns dictionary representation of object """
        if attrs:
            return {k: self.__dict__[k] for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__
