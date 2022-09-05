#!/usr/bin/python3
"""
    Student Class: Student
"""


def factorial(n: int):
    """ Factorial of n using recursion """
    if n > 1:
        return n * factorial(n - 1)
    return 1


def pascal_triangle(n):
    """ Return a list of lists of integers representing pascal's triangle """
    array = []
    for i in range(n):
        temp = []
        for j in range(i + 1):
            # nCr = n!/((n-r)!*r!)
            temp.append(factorial(i)//(factorial(j)*factorial(i-j)))
        array.append(temp)
    return array
