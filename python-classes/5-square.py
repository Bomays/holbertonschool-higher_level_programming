#!/usr/bin/python3
"""
This module defines a square class.

It is used for creation and manipulation of square objects within defined
parameters and access size attribute with diferent methods
"""


class Square:
    """A class that represent a square.

    It represents a square validating size attribute using setter method.
    The value of the size is expected to be a positive integer.

    Attributes:
        size(int): the legth of a side of the square.
    """

    def __init__(self, size=0):
        """Initialize the square with a given size

        Args:
            size(int, opt): size of square default to 0.

        Raises:
            TypeError: if size isn't an integer.
            ValueError: if size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method for size attribute.

        It gets the square size

        Returns:
            int: gets the current square size

        Raises:
            AttributeError: if size is not a
            positive int or is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square size.

        Setter method verify if input value is a positive int.
        If not it raises an error.

        Args:
            value(int): new value of square size

        Raises:
            TypeError: if size isn't an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current square area"""
        return self.size ** 2

    def my_print(self):
        """Prints current square or empty line if input is 0"""
        if self.size == 0:
            print()
            return
        else:
            for i in range(self.size):
                print("#" * self.size)
