#!/usr/bin/python3


"""
    This module creates a new matrix of the division of a matrix using matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix and the result by dividing all elements of a matrix.
    """
    result = 0
    new_matrix = []
    matrix_len = len(matrix[0])
    for row in matrix:
        new_list = []
        if matrix_len != len(row):
            raise TypeError('Each row of the matrix must have the same size')
        for element in row:
            if type(element) != int and type(element) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if type(div) != int and type(div) != float:
                raise TypeError('div must be a number')
            if div == 0:
                raise ZeroDivisionError('division by zero')
            result = round(element / div, 2)
            new_list.append(result)
        new_matrix.append(new_list)
    return new_matrix
