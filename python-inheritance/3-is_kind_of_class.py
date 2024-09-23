#!/usr/bin/python3
"""
This module checks if object is an instance
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if an instance of, or if the object
    is an instance of a class that inherited from,
    the specified class
    """
    return isinstance(obj, a_class)
