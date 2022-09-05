
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

    def to_json(self) -> dict:
        """ Returns dictionary representation of object """
        return self.__dict__
