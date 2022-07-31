#!/usr/bin/python3
""" Computes the square value of all integers of a matrix """

def square_matrix_simple(matrix=[]):
    my_matrix = matrix.copy()
    if not my_matrix:
        return my_matrix
    else:
        return [[number ** 2 for number in row] for row in my_matrix]
