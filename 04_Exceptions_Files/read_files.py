#!/usr/bin/env python3
# encoding:utf-8

# read method
file = open("filename.txt", "r")
cont = file.read()
#print(cont)
file.close()

# you provide a number as an argument to read function, This determines the
# number of "bytes" that shold be read

file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
print("Re-reading")
print(file.read())# an empty string
print("Finished")
file.close()


# To retrieve each line in a file, you can use the readlines method to
# return a list in which each element is a line in the file
file = open("filename.txt", "r")
print(file.readlines())
file.close

# use for loop

file = open("filename.txt", "r")
#print(len(file.readlines()))
for line in file:
	print(line)
file.close
