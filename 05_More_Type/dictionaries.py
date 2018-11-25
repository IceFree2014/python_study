#!/usr/bin/env python3
# encoding:utf-8

# dictionay: a built-in Python data type composed of arbitrary keys and values
# key-value
# Dictionaries are data structures used to map arbitrary keys to values
# Dictionaries can be indexed in the same way as lists, using square brackets
# containing keys.
ages = {"Dave":24, "Mary":42, "John":58}
print(ages["Dave"])
print(ages["Mary"])

# As you can see, a dictionary can store any types of data as values
primary = {
"red":[255, 0, 0],
"green":[0, 255, 0],
"blue":[0, 0, 255],
}
print(primary["red"])
#print(primary["yellow"])

empty_dictionary = {}
#print(empty_dictionary[0]) # KeyError

# Only immutable object can be used as keys to dictionaries.
# Immutable object are those that can't be changed.
bad_dict = {
[1, 2, 3]:"one two three",# Type Error
}
