#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    elif type(roman_string) is not str:
        return 0
    else:
        Rn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        length = len(roman_string)

        for i in range(length):
            value = Rn[roman_string[i]]
            if i < length - 1 and value < Rn[roman_string[i + 1]]:
                result -= value
            else:
                result += value
        return result
