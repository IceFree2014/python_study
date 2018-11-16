#!/usr/bin/env python3
# encoding:utf-8

# you can raise exceptions by using the "raise" statement
print(1)
#raise ValueError
print(2)

# Exceptions can be raised with arguments that give detail about them
name = "123"
#raise NameError("Invalid name!")


try:
	num = 5 / 0
except:
	print("An error occurred")
	raise
