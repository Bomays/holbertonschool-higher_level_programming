#!/usr/bin/python3
"""This module defines string appending process into utf-8 text file
 and return the number of characters appended"""


def append_write(filename="", text=""):
    """Create file if necessary and write or overwrite
    UTF-8 text file thanks to 'With' statement

    Args:
        filename (str): name of the given filename
        text(str): the text to append to the file

    Returns:
        int: the number of characters written
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
