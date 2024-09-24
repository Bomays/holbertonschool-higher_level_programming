#!/usr/bin/python3
"""
This module is an inheritance checker
"""


def inherits_from(obj, a_class):
    """
    Checking if object is a class instance inherited 
    directly or indirectly from the specified class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
