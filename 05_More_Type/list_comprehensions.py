#!/usr/bin/env python3
# encoding:utf-8

# List comprehensions are useful way of quickly creating lists whose contents 
# obey a simple rule.

# a list comprehension
cubes  = [i**3 for i in range(5)]
print(cubes)

# Note: List comprehensions are inspired by set-builder notation in mathematics

# A list comprehension can also contain an if statement to enforce a condition
# on values in the list.
evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

#even = [2*i for i in range(10**100)]
# It wille result in to MemoryError will be killed.
