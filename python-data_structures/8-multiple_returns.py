#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        a, b = (0, None)
    else:
        a, b = (len(sentence), sentence[0])
    return (a, b)
