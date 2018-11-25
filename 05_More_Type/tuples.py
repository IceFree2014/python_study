#!/usr/bin/env python3
# encoding:utf-8

# Tuples are very similar to lists, except that they are immutable(they can not
# be changed).Also, They are created using "parentheses",rather than square brackets
# immutable: cannot be changed after it's created.

words = ("spam", "eggs", "sausages",)
print(words[0])

# TypeError: 'tuple' object does not support item assignment  
#words[0] = "cheese" 

# list
list = ["one", "two"]

# dictionary
dict = {1: "one", 2: "two"}

# tuple
tp = ("one", "two")

# Tuples can be created without the parenttheses, by just separating the values
# with commas.
my_tuple = "one", "two", "three"
print(my_tuple[0])

tpl = ()

# tuple can be nested as lists or dictionary
tuple = (1, (1, 2, 3))
print(tuple[1])
