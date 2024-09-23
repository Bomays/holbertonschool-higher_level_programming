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
        for element in self:
            if not isinstance(element, int):
                raise TypeError("list elements must be integer")
       
        print(sorted(self))
