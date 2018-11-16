#!/usr/bin/env python3
# encoding:utf-8

# To ensure some code runs no matter what errors occur, you can use a "finally"
# statement.

try:
	print("Hello")
	print(1 / 0)
except ZeroDivisionError:
	print("Divided by zero")
finally:
	print("This code will run no matter what")

# Code in a "finally" statement even runs if an uncaught exception occurs
# in one of the preceding blocks.
try:
	print(1)
	print(10 / 0)
except ZeroDivisionError:
	print(unknown_var)
finally:
	print("This is executed last")



