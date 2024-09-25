#!/usr/bin/python3
"""Module which prints draco the dragon stuffs
using Mixin classes """


class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def __init__(self, name):
        self.name = name

    def roar(self):
        print("The dragon roars!")

    def who_roars(self):
        print("{} the dragon roars!".format(self.name))


draco = Dragon("draco")

draco.swim()
draco.fly()
draco.roar()
draco.who_roars()
