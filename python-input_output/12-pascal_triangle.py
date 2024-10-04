#!/usr/bin/python3
"""Module that returns a list of lists of integers
representing the Pascal triangle of n rows"""


def pascal_triangle(n):
    """generates a Pascal's triangle

    Args:
        n (int): number of pascal triangle rows

    Returns:
        List of list representing a pascal triangle
    """

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        up_row = triangle[i - 1]

        for j in range(1, i):
            row.append(up_row[j - 1] + up_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
