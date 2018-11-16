#!/usr/bin/env python3
# encoding:utf-8

# It is good practice to avoid wasting resources by making sure that files are
# always closed after they have been used. 
# One way of doing this is to use "try" and "finally"

try:
	f = open("filename.txt")
	print(f.read())
finally:
	f.close()

# try:
# finally:
# This ensures that the file is always closed, even if an error occurs.


# An alternative way of doing this is using "with" statements,
# This creates a temporary variable (often called f), which is
# only accessible in the indented block of the with statement.

with open("filename.txt") as f:
	print(f.read())

# Note:
# The file is automatically closed at the end of the "with" statement, 
# even if exceptions occur within it.

try:
	with open("filename2.txt") as f:
		print(f.read())
except:
	raise
