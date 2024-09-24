#!/usr/bin/python3
"""
This module defines base geometry
"""


class BaseGeometry:
    """ Class that defines base of geometry"""
    def area(self):
        """Raise exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Instance method that validates value

        Args:
            name(str): name of parameter
            value(int): value to validate

        Raises:
            TypeError and ValueError
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
