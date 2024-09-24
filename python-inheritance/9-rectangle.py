#!/usr/bin/python3
"""This module defines a rectagle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class inherited from superclass BaseGeometry
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
