#!/usr/bin/python3
"""Module that constructs an inherited FlyFishing class of
two parent classes -> Multiple inheritance with tests and MRO"""


class Fish:
    """Class defining two fish particularities through methods"""

    def swim(self):
        print("The fish is swiming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Class defining two bird particularities through methods"""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Two parents subclass defining three
    flying fish particularities through methods overriding"""

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


"""TESTS"""

flying_fish = FlyingFish()
"""Instantation of FlyingFish"""

flying_fish.fly()
flying_fish.swim()
flying_fish.habitat()

"""MRO - Method Resolution Order investigating"""
print(FlyingFish.__mro__)
