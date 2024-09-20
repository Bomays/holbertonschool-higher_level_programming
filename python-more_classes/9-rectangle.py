#!/usr/bin/python3
"""
This module defines a rectangle
"""


class Rectangle:
    """Class representing a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize Rectangle with a given width and height"""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on area

        Raises:
            TypeError: if instance is not a Rectangle one
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def __str__(self):
        """Returns a cool understandable string of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ("")

        art = ""
        symbol = self.print_symbol

        if not isinstance(symbol, str):
            symbol = str(symbol)

        for i in range(self.__height):
            art += symbol * self.__width

            if i < self.height - 1:
                art += '\n'

        return (art)

    def __repr__(self):
        """Returns the official string of the object"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Rectangle istance destructor printing message"""
        type(self).number_of_instances -= 1
        print('Bye rectangle...')
