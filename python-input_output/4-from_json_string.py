#!/usr/bin/python3
"""This module returns the object of its JSON string representation"""


import json


def from_json_string(my_str):
    """
    Converts JSON string representation to an object

    Args:
        my_str: JSON string to convert

    Returns:
       my_obj: returns python object represented by JSON string
    """
    my_obj = json.loads(my_str)
    return my_obj
