#!/usr/bin/python3
"""
This module defines base geometry classes
"""


class BaseGeometry:
    """Class that defines base of geometry"""

    def area(self):
        """Method that calculates a rectangle area

        Raise:
            Exception: Raise exception with a message
            "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer

        Args:
            name(str): name of parameter
            value(int): value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0 or equals 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
