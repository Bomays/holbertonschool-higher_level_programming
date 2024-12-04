#!/usr/bin/python3
def magic_string (string="BestSchool"):
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return string * magic_string.n
