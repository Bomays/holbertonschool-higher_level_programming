#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None

    square_matrix = []

    for row in matrix:
        new_row = []

        for element in row:
            new_row.append(element ** 2)

        square_matrix.append(new_row)

    return square_matrix
