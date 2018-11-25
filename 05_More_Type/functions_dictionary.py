#!/usr/bin/env python3
# encoding:utf-8

# dictionary keys can be assigned to different values
# Unlike lists, a new dictionary key can also be assigne a value, not just ones
# that already exist.

squares = {1: 1, 2: 4, 3: "error", 4: 16}
squares[8] = 64
squares[3] = 9 # assine a different vale
print(squares)

nums = {
1: "one",
2: "two",
3: "three",
}
# To determine whether a key is in a dictionary, you can use "in" and "not in"
# just as you can for a list.
print(1 in nums)
print("three" in nums)
print(4 not in nums)

pairs = {
"orange": [2, 3, 4],
True: False,
None: "True"
}
print(pairs.get("orange"))
print(pairs.get(True))
print(pairs.get(None))
print(pairs.get(7)) # None by default
print(pairs.get(12345, "not in dictionary")) # return "not in dictionary"

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))
