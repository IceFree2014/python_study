#!/usr/bin/env python3
# encoding:utf-8

# Exception:
# means of breaking out of the normal flow of control of a code block
# in order to handle errors or other execeptional conditions.

a = 7
b = 0
#print(a / b)

# Different exceptions are raised for different reasons
# Common exceptions:
# ImportError: an import fails;
# IndexError: a list is indexed with an out of range number;
# NameError: an unknown variable is used;
# SyntaxError: the code can't be parsed properly;
# TypeError: a function is called on a value of an inappropriate type;
# ValueError: a function is called on a value of the correct type, but 
# with an inappropriate value

# To handle exceptions, and to call code when an exception occurs, you
# can use a "try/except" statement
# If that exception occurs, the code in the "try" block stops being executed,
# and the code in the "except" block is run. If no error occurs, the code in the
# "except" block doesn't run.
try:
	a = 7
	b = 0
	print(a / b)
	print("Done calculation")
except ZeroDivisionError:
	print("An error occurred")
	print("due to zero division")


# A "try" statement can have multiple different except block

try:
	variable  = 10
	print(variable + "hello")
	print(variable / 2)
except ZeroDivisionError:
	print("Divided by zero")
except ValueError:
	print("ValueError occurred")
except TypeError:
	print("TypeError occurred")
except (ValueError, TypeError):
	print("ValueError or TypeError occurred")
except:
	print("Other Error or All Errors ")


try:
	word = "spam"
	print(word / 0)
except:
	print("An error occurred")

# Exception handling is particularly useful when dealing with user input.




