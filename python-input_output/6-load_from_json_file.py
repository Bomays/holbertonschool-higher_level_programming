#!/usr/bin/python3
"""This module writes an object to a json textfile
using 'with' statement"""


import json


def load_from_json_file(filename):
    """
    Create Object from JSON file

    Args:
        filename: the json text file
    """

    with open(filename, mode="r", encoding='utf-8') as f:
        return json.load(f)
