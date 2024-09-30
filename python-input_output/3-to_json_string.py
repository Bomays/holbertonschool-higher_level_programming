#!/usr/bin/python3
"""This module returns the JSON representation of an object(string)"""


import json


def to_json_string(my_obj):
    """
    Converts an object to its JSON string representation

    Args:
        my_obj: python object to convert

    Returns:
       str: the JSON sring representation
    """
    return json.dumps(my_obj)
