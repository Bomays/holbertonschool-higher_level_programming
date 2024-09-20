#!/usr/bin/python3
"""Module for print_square function"""


def print_square(size):
    """
    Parameters:
    Function that Prints square with the character #.
    size: is the square length size

    Returns:
    Return print square

    Raises:
    TypeError: if size is not an integer
    ValueError: if size < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
