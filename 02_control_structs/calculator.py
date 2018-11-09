#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# A simple calculator

while True:
	print("Options:")
	print("Enter 'add' to add two numbers")
	print("Enter 'subtract' to subtract two numbers")
	print("Enter 'multiply' to multiply two numbers")
	print("Enter 'divide' to divide two numbers")
	print("Enter 'quit' to end the program")
	user_input = input(":")
	if user_input == "quit":
		break
	elif user_input == "add":
		num1 = float(input("Enter a number:"))
		num2 = float(input("Enter a another number:"))
		result = str(num1 + num2)
		print("Result:", result)
	elif user_input == "subtract":
		print(user_input)
	elif user_input == "multiply":
		print(user_input)
	elif user_input == "divide":
		print(user_input)
	else:
		print("Unknown input")
