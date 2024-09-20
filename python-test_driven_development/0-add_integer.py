#!/usr/bin/python3
"""Function that adds two integer."""


def add_integer(a, b=98):
    """
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number. By default int 98.

    Returns:
    int: sum of a and b.

    Raises:
    TypeError: If a or b is not an integer or even a float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
