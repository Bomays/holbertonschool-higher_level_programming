#!/usr/bin/python3
"""
This module defines a square class.

It is used for creation and manipulation of square objects within defined
parameters and access size attribute with diferent methods
"""


class Square:
    """
    A class that represent a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with a given size

        Args:
            size(int, opt, opt): size of square default to 0
            as position tuple values.

        Raises:
            TypeError: if size isn't an integer.
            ValueError: if size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for size attribute.

        It gets the square size

        Returns:
            int: gets the current square size

        Raises:
            AttributeError: if size is not a
            positive int or is less than 0.
        """
        return self.__size

    @property
    def position(self):
        """
        Getter method for position attribute.

        It gets the square 'x,y' position

        Returns:
            int: gets the current position
            with a tuple of two integers

        Raises:
            TypeError: if position value is not
            a tuple of two positive integers
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        Setter method for square size attribute.

        Setter method verify if input value is a positive int.
        If not it raises an error.

        Args:
            value (int): new value of square size

        Raises:
            TypeError: if size isn't an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """
        Setter mehod for square position attribute.

        Setter method verify if input is a tuple of two positive integers
        If not it raises an error.

        Args:
            value (tuple(int, int)): new value of position

        Raises:
            TypeError: if position value is not
            a tuple of two positive integers
        """
        if not (
            isinstance(value, tuple)
            and len(value) == 2
            and all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates area

        Returns the current square area
        """
        return self.size**2

    def my_print(self):
        if self.size == 0:
            """Prints current square"""
            print()
            return

        print("\n" * self.position[1], end="")
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
