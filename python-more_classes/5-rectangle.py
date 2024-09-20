#!/usr/bin/python3
"""
This module defines a rectangle
"""


class Rectangle:
    """Class representing a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize Rectangle with a given width and height"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter method to retrieve rectangle width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter method setting the rectangle width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to retrieve rectangle height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter method setting the rectangle height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area"""
        return (self.width * self.height)

    def perimeter(self):
        """Returns the rectangle permimeter"""
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.width + self.height) * 2)

    def __str__(self):
        """Returns a cool understandable string of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ("")

        art = ""
        for i in range(self.__height):
            art += '#' * self.__width
            if i < self.height - 1:
                art += '\n'
        return art

    def __repr__(self):
        """Returns the official string of the object"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Rectangle istance destructor printing message"""
        print('Bye rectangle...')
