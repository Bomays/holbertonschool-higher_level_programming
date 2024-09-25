#!/usr/bin/python3
"""Module Animal_sound using abstract class and method
to defines the sound of a dog or a cat"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class reprsenting an animal"""

    @abstractmethod
    def sound(self):
        """animal sound abstract method implemanted in subclasses"""
        pass


class Dog(Animal):
    """Animal subclass for a dog"""

    def sound(self):
        """Return dog sound"""
        return "Bark"


class Cat(Animal):
    """Animal subclass for a cat"""

    def sound(self):
        """Return cat sound"""
        return "Meow"
