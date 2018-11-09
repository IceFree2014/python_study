#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Notice the colon at the end of the expression in the if statement
if 10 > 5:
	print("10 greater than 5")
print("Program ended") #the unindented statement, whic is not part of the if statement

# if statements can be nested, one inside the other.
#if expression:
#	if expression:
#		statements
#	statements
num = 12
if num > 5:
	print("Bigger than 5")
	if num <=47:
		print("Between 5 and 47")

# else statement follows an if statement, and contains code that is called
# when the if statement evaluates to False
# As with if statements, the code inside the block should be indented.
x = 4
if x == 5:
	print("Yes")
else:
	print("No")


# chain if and else statements
#if expression:
#	statements
#else:
	#if expression:
	#	statements
	#else:
		#if expression:
		#	statements
		#else:
		#	statements	

num = 7
if num == 5:
	print("Number is 5")
else:
	if num == 11:
		print("Number is 11")
	else:
		if num == 7:
			print("Number is 7")
		else:
			print("Number isn't 5, 11 or 7")

# elif ---short for else if
#if expression:
#	statements
#elif expression:
#	statements
#elif expression:
#	statements
#elif expression:
#	statements
#else:
#	statements

num = 7
if num == 5:
	print("Number is 5")
elif num == 11:
	print("Number is 11")
elif num == 7:
	print("Number is 7")
else:
	print("Number isn't 5, 11 or 7")
	
	
	
