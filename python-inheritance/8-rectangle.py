#!/usr/bin/python3
"""This module defines a rectagle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class inherited of superclass BaseGeometry
    that defines a rectangle
    """

    def __init__(self, width, height):
        """Initializing method"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
