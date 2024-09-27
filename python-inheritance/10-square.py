#!/usr/bin/python3
"""A class Square which is a Rectangle heritage"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Subclass inherited of rectangle subclass that defines a square"""

    def __init__(self, size):
        """Initializing square instance

        Args:
            size (int): height and width square
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method that calculates a rectangle area
        Returns:
            int: square area
        """
        return self.__size ** 2
