#!/usr/bin/python3
"""Module Counted Iterator that permits to iterate a list
and return item with a count when each item is passed"""


class CountedIterator:
    """ Counted Iterator class that permits counting a list iteration"""
    def __init__(self, some_iterable):
        """Constuctor initializing two attributes"""
        self.iterator = iter(some_iterable)
        self.count = 0

    def get_count(self):
        """Method to get the count"""
        return self.count

    def __iter__(self):
        """Method used for iteration"""
        return self

    def __next__(self):
        """Method used for incrementing"""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration


test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count_iteration = CountedIterator(test_list)
"""Test instantiation of CounedIterator using a list from 1 to 10"""

try:
    while True:
        item = next(count_iteration)
        print("Item: {}, Count: {}".format(item, count_iteration.get_count()))
except StopIteration:
    print("Iteration is complete, finished or whatever!")
