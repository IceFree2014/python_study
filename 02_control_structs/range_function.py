#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# The "range" function creates a sequential list of numbers.
# list is a functions
# Note: The call to "list" is necessary because "range" by itself creates a 
# "range object", and this must be converted to a list if you want to use it
# as one.
numbers = list(range(10))
print(numbers)

# range with two argument
numbers = list(range(3, 8))# [3,8)
print(numbers)
print(range(20) == range(0, 20))


# range with three argument
# range can have a third argument, which determines the interval of the 
# sequence produced. This third argument must be an integer.
numbers = list(range(5, 20, 2))
print(numbers)

numbers = list(range(5, 20, 3))
print(numbers)


