#!/usr/bin/env python3
# encoding:utf-8

# write method
# To write to files you use the write method, which writes a string to the file.
# The "w" mode will create a file, if it does not already exist
file = open("newfile.txt", "w")
file.write("This has been written to a file.")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()

file = open("newfile.txt", "w")
file.write("Some new text.")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()

# It will delete the content
file = open("newfile.txt", "w")
file.close()

msg = "Hello world"
file = open("newfile.txt", "w")
# The "write" method return the number of bytes written to a file.
amount_written = file.write(msg)
amount_written += file.write("!")
# To write something other than a string, it needs to be converted to 
# a string first.
amount_written += file.write(str(123))
print(amount_written)
file.close()
