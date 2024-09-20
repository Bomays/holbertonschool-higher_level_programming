#!/usr/bin/python3
"""Function that divides all element of a matrix by a given number"""


def matrix_divided(matrix, div):
    """
    Parameters:
    matrix (list of lists): The matrix to be divided.
    div (int or float): The number to divide by.

    Returns:
    list of lists: A new matrix with all elements divided by div,
    rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is zero.
    """

    # matrix type
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # matrix elements type
    if not all(isinstance(num, (int, float))
               for row in matrix for num in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # line length
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # div type
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # division by 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
        new_matrix.append(new_row)
    return new_matrix
