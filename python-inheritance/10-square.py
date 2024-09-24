#!/usr/bin/python3
"""A class Square which is a Rectangle heritage"""
Rectangle = __import__('9-retangle').Rectangle


class Square(Rectangle):
    """
    Subclass inherited of rectangle subclass that defines a square

    Attributes:
        __size(int): size (length) of a square
    """

    def __init__(self, size):
        """Initializing square instance

        Args:
        size(int): zie of a square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0 or equal to 0
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
        """ Initialize Rectangle width and height with size"""

    def area(self):
        """Method that calculates a rectangle area

        Returns:
            int: square area
        """
        return (self.__size * 2)

    def __str__(self):
        """Method with __str__ that returns a string
            representation of a square

        Returns:
            str: informal string representation of a square
        """
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
