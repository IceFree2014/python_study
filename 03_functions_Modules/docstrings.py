#!/usr/bin/env python3
# encoding:utf-8

# Docstrings(documentation strings) serve a similar purpose to comments
# as they are designed to explain code.
# However, they are more specific and have a different syntax.
# They are created by putting a multiline string containing an explanation of
# the function below the function's first line.

""" I am a test for mutiline string
    commetns
    end.
	This string will be retain when the program at run time
    so don't do it for mutiline string comments
"""
# unlike conventional commetnts, "docstrings" are retained throughout
# the runtime of the program. 
# This allows the programmer to inspect these comments at run time

def shout(word):
 """
 Prinr a word with an
 exclamation mark following it.
 """
 print(word + "!")

shout("spam")
