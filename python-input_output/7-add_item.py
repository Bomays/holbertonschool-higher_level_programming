#!/usr/bin/python3
"""This module writes an object to a json textfile
using 'with' statement"""



import json
import sys


def load_from_json_file(filename):
    """
    Create Object from JSON file

    Args:
        filename: the json text file
    """

    with open(filename, mode="r", encoding='utf-8') as f:
        my_obj = json.load(f) 
        """add: (f, object_pairs_hook=OrderedDict) to keep order"""
    return my_obj


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

if __name__ == "__main__":
    filename = "add_item.json"

    try:
        items = load_from_json_file(filename)
    except FileNotFoundError or json.JSONDecodeError:
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, filename)
