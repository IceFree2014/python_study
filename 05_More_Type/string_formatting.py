#!/usr/bin/env python3
# encoding:utf-8

# So far, to combine strings and non-string, you've converted the non-strings to
# strings and added them.
# String formatting provides a more powerful way to embed non-string with strings.
# String formattting uses a string's "format" method to substitute a number of
# arguments in the string.

# string fromating
nums = [4, 5, 6]
msg = "Numbers:{0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)

# Note: Each argument of the format function is placed in the string at the 
# corresponding position,which is determined using the curly braces {}

print("{0}{1}{0}".format("abra", "cad"))

a = "{x},{y}".format(x=5, y=12)
print(a)
str = "{c},{b},{a}".format(a=5, b=9, c=7)
print(str)
