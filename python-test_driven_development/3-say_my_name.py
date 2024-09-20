#!/usr/bin/python3
'''Function that prints Prints "My name is <first_name> <last_name>"'''


def say_my_name(first_name, last_name=""):
    """
    Parameters:
    first_name (str): The first name to be printed.
    last_name (str): The last name to be printed.

    Returns:
    list of lists: A new matrix with all elements divided by div,
    rounded to 2 decimal places.

    Raises:
    TypeError: If either first_name or last_name is not a string.

    Returns:
    None: This function only prints output and does not return a value.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
