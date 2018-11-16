#!/usr/bin/env python3
# encoding:utf-8
# An assertion is a sanity-check that you can turn on or turn off 
# when you have finished testing the program.
# Assertions are carried out through use of the "assert" statement.

# An expression is tested, and if the result comes up false, an exception
# is raised.

print(1)
assert 2 + 2 == 4
print(2)
#assert 1 + 1 == 3 # The expression is false
print(3)

# Programmers often place assertions at the start of a function to check
# for valid input, and after a function call to check for valid output

# The "assert" can take a second argument that is passed to the AssertionError
# raised if the assertion fails
temp = -10
assert(temp >= 0), "Colder than absolute zero!"
