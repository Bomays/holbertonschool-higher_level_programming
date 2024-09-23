#!/usr/bin/python3
"""
This module defines a list
"""

class MyList(list):
    """
    Built-in list
    """
    def __init_(self):
        '''Initialize the class callin superclass'''
        super().__init__()

    def print_sorted(self):
            '''Prints sorted list'''
            print(sorted(self))
