#!/usr/bin/python3
"""
This module defines base geometry classes
"""


class BaseGeometry:
    """ Class that defines base of geometry"""

    def integer_validator(self, name, value):
        """Validates that value is a positive integer

        Args:
            name(str): name of parameter
            value(int): value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0 or equals 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Subclass inherited of superclass BaseGeometry
    that defines a rectangle

    Attributes:
        __width(int): width rectangle
        __height(int): height rectangle
    """

    def __init__(self, width, height):
        """Initializing a Rectangle instance

        Args:
            width(int):  width rectangle
            height(int): height rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method that calculates a rectangle area

        Returns:
            int: the area of a rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """Method with __str__ that returns a string
            representation of a rectangle

        Returns:
            str: informal string representation of a rectangle
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def print(self):
        """Prints the string representation of a rectangle"""
        print(self.__str__())


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
        return (self.__size ** 2)

    def __str__(self):
        """Method with __str__ that returns a string
            representation of a square

        Returns:
            str: informal string representation of a square
        """
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
    