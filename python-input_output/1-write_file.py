#!/usr/bin/python3
"""This module defines string writing utf-8 text file
process and return the number of characters written"""


def write_file(filename="", text=""):
    """Create file if necessary and write or overwrite
    UTF-8 text file thanks to 'With' statement

    Args:
        filename (str): name of the given filename
        text(str): the text to write in the given file

    Returns:
        int: the number of characters written
    """

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
