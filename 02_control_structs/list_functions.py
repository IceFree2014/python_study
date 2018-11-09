#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Another way of altering lists is using the "append" method
# This adds an item to the end of an existing list.
nums  = [1, 2, 3]
# The dot before append is there because it is a method of the list class.
nums.append(4)
print(type(nums))
print(nums)

# To get the number of items in a list, you can use the len function.
# Unlike append, len is a normal function, rather than a method.
# This means it is writen before the list it is being called on, without a dot.
nums = [1, 3, 5, 2, 4]
print(len(nums))

# len is a function
print(len("Hello world!"))

# The "insert" method is similar to append, except that it allows you to insert
# a new item at any position in the list, as opposed to just at the end.
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)

# The "index" method finds the "first" occurrence of a list item and returns its
# index. if the item isn't in the list, it raises a ValueError. 
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('z'))

# There are a few more useful functions and methods for list.
# max(list): Returns the list item with the maximum value
# min(list): Returns the list item with the minimum value
# list.count(obj): Returns a count of how many times an item occurs in a list
# list.remove(obj): Removes an object form a list
# list.reverse(): Reverses object in a lit

