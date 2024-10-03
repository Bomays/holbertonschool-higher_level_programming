#!/usr/bin/python3
"""This module defines a class student defining a student"""


import sys
import json


class Student:
    def __init__(self, first_name, last_name, age):
        """initialize Student with attributes"""
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):
        """Returns a dic. representation of Student instance
        If attrs is a list of strings, only attribute names
        contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved."""
        if isinstance(attrs, list):
            return {
                attr: self.__dict__[attr]
                for attr in attrs if attr in self.__dict__
            }
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
