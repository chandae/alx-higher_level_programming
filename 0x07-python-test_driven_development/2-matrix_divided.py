#!/usr/bin/python3
"""
    2-matrxt_divided: matrix_divided - divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
        Divides all elements of a matrix by div

        Args:
            matrix: first argument
            div: second argument
        Returns:
            new matrix with each element divided by div
    """

    new_matrix = []
    error_1 = "matrix must be a matrix (list of lists) of integers/floats"
    error_2 = "Each row of the matrix must have the same size"

    # Matrix must be a list of lists of integers or floats
    if not (isinstance(matrix, list)) or not matrix:
        raise TypeError(error_1)
    for row in matrix:
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error_1)

    # Each row of the matrix must be the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError(error_2)

    # div must be a number and cannot be zero(0)
    if not (isinstance(div, int)) and not (isinstance(div, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")

    # Divide the elements by div
    for row in matrix:
        temp = [float("{:.2f}".format(num / div)) for num in row]
        new_matrix.append(temp)

    return new_matrix
