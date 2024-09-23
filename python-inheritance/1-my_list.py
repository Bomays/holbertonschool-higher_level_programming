#!/usr/bin/python3
"""
This module defines a list
"""

class MyList(list):
    """
    Built-in list
    """
    def print_sorted(self):
            '''Prints sorted list'''
            print(sorted(self))
