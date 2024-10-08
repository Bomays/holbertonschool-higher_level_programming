# Python - import & modules

$~$

<p align="center">
<img src="https://github.com/Bomays/holbertonschool-higher_level_programming/blob/9441bc9f0855463ba8b62e4f2bc7e68090566757/images/python-logo-only.png" alt="Python" width="100"/>
</p>


## General
```
Why Python programming is awesome
How to import functions from another file
How to use imported functions
How to create a module
How to use the built-in function dir()
How to prevent code in your script from being executed when imported
How to use command line arguments with your Python programs
```


### 0. Import a simple function from a simple file
File: 0-add.py

Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3

```
> Requirements

You have to use print function with string format to display integers
You have to assign:
the value 1 to a variable called a
the value 2 to a variable called b
and use those two variables as arguments when calling the functions add and print
a and b must be defined in 2 different lines: a = 1 and another b = 2
Your program should print: <a value> + <b value> = <add(a, b) value> followed with a new line
You can only use the word add_0 once in your code
You are not allowed to use * for importing or __import__
Your code should not be executed when imported - by using __import__
```


### 1. My first toolbox!
File: 1-calculation.py

Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.

```
> Requirements

Do not use the function print (with string format to display integers) more than 4 times
You have to define:
the value 10 to a variable a
the value 5 to a variable b
and use those two variables only, as arguments when calling functions (including print)
a and b must be defined in 2 different lines: a = 10 and another b = 5
Your program should call each of the imported functions. See example below for format
the word calculator_1 should be used only once in your file
You are not allowed to use * for importing or __import__
Your code should not be executed when imported
```

### 2. How to make a script dynamic!
File: 2-args.py

Write a program that prints the number of and the list of its arguments.

```
> Requirements

The output should be:
Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
: (or . if no arguments were passed) followed by
a new line, followed by (if at least one argument),
one line per argument:
the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
Your code should not be executed when imported
The number of elements of argv can be retrieved by using: len(argv)
You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.
```

### 3. Infinite addition
File: 3-infinite_add.py

Write a program that prints the result of the addition of all arguments

```
> Requirements

The output should be the result of the addition of all arguments, followed by a new line
You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
Your code should not be executed when imported
Last but not least, your program should also handle big numbers.
```

### 4. Who are you?
File: hidden_4.pyc

Write a program that prints all the names defined by the compiled module hidden_4.pyc

```
> Requirements

This task must be done on the sandbox only
File 4-hidden_discovery.py must be located on the folder /tmp/
You should print one name per line, in alpha order
You should print only names that do not start with __
Your code should not be executed when imported
```


### 5. Everything can be imported

File: 5-variable_load.py

Write a program that imports the variable a from the file variable_load_5.py and prints its value.

```
> Requirements

You are not allowed to use * for importing or __import__
Your code should not be executed when imported
```
