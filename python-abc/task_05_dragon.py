#!/usr/bin/python3
"""Module which prints draco the dragon stuffs
using Mixin classes """


class SwimMixin:
    """Mixin class for dragon swimming"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin class for dragon flying"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Inherited class for dragon roar"""

    def __init__(self, name="draco"):
        """Initialize dragon with name"""
        self.name = name

    def roar(self):
        print("The dragon roars!")


"""TESTS"""

draco = Dragon("draco")
"""Instantiation of Dragon"""

draco.swim()
draco.fly()
draco.roar()
