#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        max_elem = my_list[0]

        for element in my_list[1:]:
            if element > max_elem:
                max_elem = element
        return (max_elem)

    return (None)
