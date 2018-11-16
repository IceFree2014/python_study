#!/usr/bin/env python3
# encoding:utf-8

# Before a file can be edited, it must be opened, using the "open" function

# if the file is in the current working directory,you can
# specify only its name
path = "filename.txt" 
myfile = open(path)

# You can specify the "mode" used to open a file by applying a second argument
# "mode" "r" means open it read mode, which is the default.
# "mode" "w" means write mode, for rewriting the contents of a file.
# "mode" "a" means append mode, for adding new content to the end of the file.
# "mode" "b" means a mode opens it in binary mode, which is used for 
# non-text files(such as image and sound files)

# write mode
open(path, "w")

# read mode
open(path, "r")
open(path)

# binary write mode
open(path, "wb")

# Note:
# You can use the + sign with each of the modes above to give them extra access to files. For example, 
# r+ opens the file for both reading and writing.

# +mode
open(path, "r+") # for both reading and writing

# Once a file has been opened and used, you should close it.
# This is done with the "close" method of the file object.
file = open(path, "w")
# do stuff to the file
file.close()
