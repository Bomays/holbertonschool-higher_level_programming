#!/usr/bin/python3
"""
This module defines base geometry
"""


class BaseGeometry:
    """ Class that defines base of geometry"""

    def integer_validator(self, name, value):
        """Instance method that validates value

        Args:
            name(str): name of parameter
            value(int): value to validate

        Raises:
            TypeError: if value isnot an integer
            ValueError: if value is less than 0 or equals 0
        """
        if isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Subclass inherited from superclass BaseGeometry
    that defines a rectangle
    """

    def __init__(self, width, height):
        """Initializing method"""

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method that calculate rectangle area"""
        return (self.__width * self.__height)

    def __str__(self):
        """Method with __str__ that returns values"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def print(self):
        """Method that prints rectangle values with __str__"""
        print(self.__str__())


class Square(Rectangle):
    """
    Subclass inherited from rectangle subclass BaseGeometry
    that defines a square
    """

    def __init__(self, size):
        """Initializing method
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
        """ Initialize Rectangle width and height with size"""

    def area(self):
        """Method that calculate rectangle area"""
        return super().area()
        """Return that use area method from Rectangle"""

    def __str__(self):
        """Method with __str__ that returns square values"""
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def print(self):
        """Method that prints square values with __str__"""
        print(self.__str__())
