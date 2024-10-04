#!/usr/bin/python3
"""Module that serializes and deserializes custom Python
objects using the pickle module wich works with binary data,
and OS module which is a file and directory, process
and shell cmd module manager"""


import os
import pickle


class CustomObject:
    "Main class CustomObject"
    def __init__(self, name, age, is_student):
        """Initialize objects with name, age and is_student attributes"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """Method that takes a filename as its parameter and using PICKLE
        module it serialize the current instance of the object and
        save it to the provided file"""
        with open(filename, mode="wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """Class method that takes a filename as parameter
        and load and return an instance of the CustomObject from
        the provided filename using PICKLE"""
        if not os.path.exists(filename):
            print("Error: {} missing".format(filename))
            return None

        try:
            with open(filename, mode="rb") as f:
                return pickle.load(f)
        except (pickle.UnpicklingError, OSError, EOFError) as e:
            print("Error while Unpickling: {}".format(e))

    def display(self):
        """Display method that prints out the object’s attributes """
        print("Name: {}, Age: {}, Is Student: {}".format
              (self.name, self.age, self.is_student))
