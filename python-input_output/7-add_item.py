#!/usr/bin/python3
"""This module  adds all arguments to a Python list,
and then save them to a file, and create it if does not
already exists"""


import sys


load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except (FileNotFoundError, ValueError):
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
