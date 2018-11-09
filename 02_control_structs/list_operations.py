#!/usr/bin/env python3
# -*- coding:utf-8 -*-

nums = [7, 7, 7, 7, 7]
print(nums)
nums[2] = 5
print(nums)

# lists can be added and multiplied in the same way as strings
nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

# Note:
# Lists and strings are similar in many ways - strings can be thought of as lists
# of characters can't be changed.
str = "Hello wrold!"
print(str[0])
print(type(str[0]))
#str[0] = 'h'
print(str[0])

# To check if an item is in a list, the "in" operator can be used. 
# It returns Ture if the item occurs one or more times in the list, 
# and False if it doesn't.
# The "in" operator is also used to determine whether or not 
# a string is substring of another string. 
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

# To check if an item is not in a list, you can use the "not" operator
# x not in y
nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)
