#!/usr/bin/env python3
# encoding:utf-8

# In addition to using pre-defined functions, 
# you can create your own functions by using the "def" statement

# The code block within every function starts with a colon(:) and is indented.
# my_func() // You must define functions before they are called.
def my_func():
 print("spam")
 print("spam")
 print("spam")

my_func()


# defines a function that take one argrument
def print_with_exclamation(word):
 print(word + "!")

print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")


# define functions with more than one argument
def print_sum_twice(x, y):
 print(x + y)
 print(x + y)

print_sum_twice(5, 8)

# return form functions
def max(x, y):
 if x >= y:
    return x
 else:
    return y

print(max(4, 7))
z = max(8, 5)
print(z)


# Comments
x = 365
y = 7
# this is a comment

# Python doesn't have general purpose multiline comments, as do programing 
# languages such as C





