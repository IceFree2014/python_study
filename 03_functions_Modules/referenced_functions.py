#!/usr/bin/env python3
# encoding: utf-8

def multiply(x, y):
 return x * y

a = 4
b = 7
# asssign function to a variable
operation = multiply
# referenced by variable operation
print(operation(4, 7))

# Functions can also be used as arguments of other functions
def add(x, y):
	return x + y

def do_twice(func, x, y):
	return func(func(x, y), func(x, y))

a = 5
b = 10
print(do_twice(add, a, b))

