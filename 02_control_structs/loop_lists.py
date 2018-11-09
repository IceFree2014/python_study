#!/usr/bin/env python3
# -*- coding:utf-8 -*-
words = ["hello", "world", "spam", "eggs"]
counter = 0
max_index = len(words) - 1

while counter <= max_index:
	word = words[counter]
	print(word + "!")
	counter = counter + 1

# Iterating through a list using a while loop requires quite a lot of code
# so Python provides the for loop as shortcut that accomplishes the same
# thing.
print("for loop:")
words = ["hello", "world", "spam", "eggs"]
for word in words:
	print(word + '!')

# The for loop is commonly used to repeat some code a certain number of times.
# You don't need to call list on the range object when it is used in a for loop,
# because it isn't being indexed, so a list isn't required.
for i in range(5):
	print("Hello!")
