#!/usr/bin/python3
"""Module that explore serialization and
deserialization using XML as an alternative
format to JSON"""


import xml.etree.ElementTree as ET
import json


def serialize_to_xml(dictionary, filename):
    """Method that takes a Python dictionary and a filename as parameters.
    It should serialize the dictionary into XML and save it to
    the given filename."""

    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Method that takes a filename as its parameter,
    read the XML data from that file, and return a deserialized
    Python dictionary."""

    tree = ET.parse(filename)
    root = tree.getroot()
    result_dict = {}

    for child in root:
        result_dict[child.tag] = child.text

    return result_dict
