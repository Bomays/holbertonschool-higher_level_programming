#!/usr/bin/python3
"""This module writes an object to a json textfile
using 'with' statement"""


import json


def save_to_json_file(my_obj, filename):
    """
    Converts JSON string representation to an object

    Args:
        my_obj: the python object to serialize in a json text file

    Returns:
       filename: the json text file
    """

    with open(filename, mode="w", encoding='utf-8') as f:
        json.dump(my_obj, f)
