#!/usr/bin/python3
"""This module defines reading utf-8 text file process"""

def read_file(filename=""):
    """Reads and write UTF-8 text file thanks to 'With' statement"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
