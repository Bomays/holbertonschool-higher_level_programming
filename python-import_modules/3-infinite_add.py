#!/usr/bin/python3
if __name__ == "__main__":
    import sys


result = sum(int(arg) for arg in sys.argv[1:])
'''
> int(arg) convert each argument into integer
> sys.argv[1:] take in consideration ararguments in the passed
argument listed by user, avoiding arg[0] which is the name
of the prog print(result)
'''
print(result)
