#!/usr/bin/python3
"""
This module defines a singly linked list.
"""


class Node:
    """
    A class that represent a node.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize the node with a given data

        Args:
            data(int, opt, opt).

        Raises:
            TypeError: if data isn't an integer.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for data attribute.
        """
        return self.__data

    @property
    def next_node(self):
        """
        Getter method for next_node attribute.
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """
        Setter method for square size attribute.
        
        Raises:
            TypeError: if size isn't an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """
        Setter mehod for square position attribute.

        Raises:
            TypeError: if next_node is not a node
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """
    A class that represent a singly linked list.
    """

    def __init__(self):
        """
        Initialize the list with empty head
        """
        self.__head = None

    def __str__(self):
        """
        Initialize the list with empty head
        """
        node = self.__head
        result = []
        while node is not None:
            result.append(str.node.data)
            node = node.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Setter method for square size attribute.
        """
        new_node = Node(value)



