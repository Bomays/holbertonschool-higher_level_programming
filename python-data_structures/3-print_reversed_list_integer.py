#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        a = len(my_list)-1
        while a >= 0:
            print("{:d}".format(my_list[a]))
            a -= 1
