#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Lists are another type of object in Python.
# They are used to store an indexed list of items.
# A list is created using square brackets(方括号) with commas(逗号) separatin items
# The certain item in the list can be accessed by using its index in square brackets.

words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

empty_list = []
print(empty_list)

# Typically, a list will contain items of a single items type, but 
# it is also possible to include several different types.
# Lists can also be nested within other lists
number = 3
things = ["string", 0, [1, 2, number], 4.56, [7, 8, [9, 10]]]
print(things[0])
print(things[0][0])
print(things[1])
print(things[2])
print(things[2][2])
print(things[3])
print(things[4][0])
print(things[4][1])
print(things[4][2][0])
print(things[4][2][1])

# indexing out of the bounds of possible list values cause an IndexError
# Some types such as string, can be indexed like lists. Index strings behaves as
# though you are indexing a list containing each character in the string.
str = "Hello world!"
print(type(str))
print(str[6])
print(str[11])
#print(str[12])
