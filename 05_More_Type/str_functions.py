#!/usr/bin/env python3
# encoding:utf-8

# Python contains many useful build-in functions and methods to accomplish
# common tasks.

# join-joins a list of strings with another string as a separator.
print(",".join(["spam", "eggs", "ham"]))
# prints "spam, eggs,ham"

# replace- replaces one substring in a string with another
print("Hello ME".replace("ME", "world"))
# prints "Hello world"

# startswith and endswith- determine if there is a substring at the start and end
# of a string,respectively.
print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

# To change the case of a string, you can use lower and upper.
print("This a sentence.".upper())
# prints "THIS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
# prints "an all caps sentence"

# The method "split" is  the opposite of join, turning a string with a certain
# separator into a list.
print("spam, eggs, ham".split(","))
# prints "['spam', ' eggs', ' ham']"
