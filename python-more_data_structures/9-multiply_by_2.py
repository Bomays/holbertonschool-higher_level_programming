#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    multiplied_dictionnary = {}

    for key, value in a_dictionary.items():
        multiplied_dictionnary[key] = value * 2

    return multiplied_dictionnary
