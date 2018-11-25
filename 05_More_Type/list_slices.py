#!/usr/bin/env python3
# encoding:utf-8

# List slices provide a more advanced way of retrieving values from a list.
# Basic list slicing involves indexing a list with two colon-separated integers.
# This returns a new list containing all the values in the old list between the
# indices.

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Like the arguments to "range", the first index provided in a slice is included
# in the result but the second isn't
new_list = squares[2:6] # 2-5
new_list = squares[3:8] # 3-7
new_list = squares[0:1] # 0
print(new_list)
print(type(new_list))


squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# If the first number in a slice is omitted, it is taken to be the start of the list
# If the second number is omitted,it is taken to be the end.
print(squares[:7])
print(squares[7:])

# Note: Slicing can also be done on tuples
tupl = (1, 2, 3, 4, 5, 6, 7)
print(tupl[:7])
print(tupl[4:])

# List slices can also have a third number, representing the step, to include
# only alrenate values in the slice.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
slices = squares[::2]
slices = squares[2:8:3] # 4, 9, 16, 25, 36, 49
slices = squares[1::4] # 1, 4, 9, 16, 25, 36, 49, 64, 81
print(slices)
print(type(slices))

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Negative values can be used in list slicing(and normal list indexing).
# When negative values are used for the first and second values in a slice
# (or a normal index),they count from the end of the list.
print(squares[1: -1])
print(squares[-3:])
# If a negative value is used for the step, the slice is done backwards.
# Using [::-1] as a slice is a common and idiomatic way to reverse a list.
print(squares[::-1])
print(squares[-3::-1])
print(squares[7:5:-1])
