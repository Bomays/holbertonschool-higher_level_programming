# Python - Test-driven development

$~$

<p align="center">
<img src="https://github.com/Bomays/holbertonschool-higher_level_programming/blob/main/python-test_driven_development/Image/doctest%20none%20official%20and%20Ai%20generated%20logo.jpeg?raw=true"alt="Python" width="120"/>
</p>


## General
```
Why Python programming is awesome
What’s an interactive test
Why tests are important
How to write Docstrings to create tests
How to write documentation for each module and function
What are the basic option flags to create tests
How to find edge cases
```

## Requirements

### Python Test Cases

```
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: python3 -m doctest ./tests/*

- All your modules should have a documentation
  (python3 -c 'print(__import__("my_module").__doc__)')

- All your functions should have a documentation
  (python3 -c 'print(__import__("my_module").my_function.__doc__)')

- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of
  the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case
– The Checker is checking for tests!
```


## Testing with a .txt :

 Usage Exemples :

 $~$
> Testing bash command: python3 -m doctest -v ./tests/0-add_integer.txt | tail -2

> Tesing bash command with details outputed: python3 -m doctest -v ./tests/0-add_integer.txt

$~$
>Text File : 

```
>>> print_square = __import__('4-print_square').print_square

# Testing normal size
>>> print_square(3) 
###
###
###

# Testing size 0
>>> print_square(0)


# Testing size 1
>>> print_square(1)
#

# Testing negative size
>>> print_square(-1)
Traceback (most recent call last):
ValueError: size must be >= 0

# Testing no args 
>>> print_square()
Traceback (most recent call last):
TypeError: print_square() missing 1 required positional argument: 'size'

# Testing None size
>>> print_square(None)
Traceback (most recent call last):
TypeError: size must be an integer

# Testing float size
>>> print_square(3.5)
Traceback (most recent call last):
TypeError: size must be an integer

# Testing string size
>>> print_square("3")
Traceback (most recent call last):
TypeError: size must be an integer
```


> Python file

```
#!/usr/bin/python3
"""Module for print_square function"""


def print_square(size):
    """
    Parameters:
    Function that Prints square with the character #.
    size: is the square length size

    Returns:
    Return print square

    Raises:
    TypeError: if size is not an integer
    ValueError: if size < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
```
