#!/usr/bin/python3
"""Module Shape that permit to calculate and print
Rectangle and Circle Area and perimeter"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class representing a shape"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


def shape_info(shape):
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))


if __name__ == "__main__":
    """Instantation of Shape objects"""
    circle = Circle(2)
    rectangle = Rectangle(2, 3)

    print("Circle Info:")
    shape_info(circle)

    print("Rectangle Info:")
    shape_info(rectangle)
