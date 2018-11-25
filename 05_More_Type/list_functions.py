#!/usr/bin/env python3
# encoding:utf-8

nums = [55, 44, 33, 22, 11]
if all([i > 5 for i in nums]):
	print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
	print("At least on is even")

# The function "enumerate" can be used to iterate through the values and indices
# of a list simultaneously.
for v in enumerate(nums):
	print(v)
