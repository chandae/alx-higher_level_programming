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
            return {k: self.__dict__[k] for k in self.__dict__.keys() & attrs}
        else:
            return self.__dict__

student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)