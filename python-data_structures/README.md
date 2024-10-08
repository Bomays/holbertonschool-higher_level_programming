# Python-data_structures

$~$

<p align="center">
<img src="https://github.com/Bomays/holbertonschool-higher_level_programming/blob/9441bc9f0855463ba8b62e4f2bc7e68090566757/images/python-logo-only.png" alt="Python" width="100"/>
</p>

## General
```
What are lists and how to use them
What are the differences and similarities between strings and lists
What are the most common methods of lists and how to use them
How to use lists as stacks and queues
What are list comprehensions and how to use them
What are tuples and how to use them
When to use tuples versus lists
What is a sequence
What is tuple packing
What is sequence unpacking
What is the del statement and how to use it
```


### 0. Print a list of integers
File: 0-print_list_integer.py

Write a function that prints all integers of a list.

```
Requirements:

Prototype: def print_list_integer(my_list=[]):
Format: one integer per line. See example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers
```


### 1. Secure access to an element in a list
File: 1-element_at.py

Write a function that retrieves an element from a list.

```
Requirements:

Prototype: def element_at(my_list, idx):
If idx is negative, the function should return None
If idx is out of range (> of number of element in my_list), the function should return None
You are not allowed to import any module
You are not allowed to use try/except
```

### 2. Replace element
File: 2-replace_in_list.py

Write a function that replaces an element of a list at a specific position.

```
Requirements:

Prototype: def replace_in_list(my_list, idx, element):
If idx is negative, the function should not modify anything, and returns the original list
If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
You are not allowed to import any module
You are not allowed to use try/except
```

### 3. Print a list of integers... in reverse!
File: 3-print_reversed_list_integer.py

Write a function that prints all integers of a list, in reverse order.

```
Requirements:

Prototype: def print_reversed_list_integer(my_list=[]):
Format: one integer per line. See example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers
```

### 4. Replace in a copy
File: 4-new_in_list.py

Write a function that replaces an element in a list at a specific position without modifying the original list.

```
Requirements:

Prototype: def new_in_list(my_list, idx, element):
If idx is negative, the function should return a copy of the original list
If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
You are not allowed to import any module
You are not allowed to use try/except
```

### 5. Can you C me now?
File: 5-no_c.py

Write a function that removes all characters c and C from a string.

```
Requirements:

Prototype: def no_c(my_string):
The function should return the new string
You are not allowed to import any module
You are not allowed to use str.replace()
```

### 6. Lists of lists = Matrix
File: 6-print_matrix_integer.py


Write a function that prints a matrix of integers.

```
Requirements :

Prototype: def print_matrix_integer(matrix=[[]]):
Format: see example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers
```

### 7. Tuples addition
File: 7-add_tuple.py

Write a function that adds 2 tuples.

```
Requirements:

Prototype: def add_tuple(tuple_a=(), tuple_b=()):
Returns a tuple with 2 integers:
The first element should be the addition of the first element of each argument
The second element should be the addition of the second element of each argument
You are not allowed to import any module
You can assume that the two tuples will only contain integers
If a tuple is smaller than 2, use the value 0 for each missing integer
If a tuple is bigger than 2, use only the first 2 integers
```


### 8. More returns!
File: 8-multiple_returns.py

Write a function that returns a tuple with the length of a string and its first character.

```
Requirements:

Prototype: def multiple_returns(sentence):
If the sentence is empty, the first character should be equal to None
You are not allowed to import any module
```

### 9. Find the max
File: 9-max_integer.py

Write a function that finds the biggest integer of a list.

```
Rquirements:

Prototype: def max_integer(my_list=[]):
If the list is empty, return None
You can assume that the list only contains integers
You are not allowed to import any module
You are not allowed to use the builtin max()
```

### 10. Only by 2
File: 10-divisible_by_2.py

Write a function that finds all multiples of 2 in a list.

```
Requirements:

Prototype: def divisible_by_2(my_list=[]):
Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2
The new list should have the same size as the original list
You are not allowed to import any module
```

### 11. Delete at
File: 11-delete_at.py

Write a function that deletes the item at a specific position in a list.

```
Requirements:

Prototype: def delete_at(my_list=[], idx=0):
If idx is negative or out of range, nothing change (returns the same list)
You are not allowed to use pop()
You are not allowed to import any module
```

### 12. Switch
File: 12-switch.py

Complete the source code in order to switch value of a and b
```
Requirements:

You can find the source code here
Your code should be inserted where the comment is (line 4)
Your program should be exactly 5 lines long
```