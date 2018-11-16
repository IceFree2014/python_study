#!/usr/bin/env python3
# encoding:utf-8

# Modules are pieces of code that other people have 
# writen to fulfill common tasks.

# The basic way to use a module is to add "import module_name" at
# the top of your code, and then using "module_name.var" to access functions
# and values with the name "var" in the module.

# The code uses the "randint" function defined in the random to 
# print 5 random numbers in the range 1 to 6
import random
for i in range(5):
 value = random.randint(1, 6)
 print(value)


# There is another kind of "import" that can be used if you only need certain 
# functions from a module. These take the form "from module_name import var"
# and then "var" can be used as if it were defined normally in your code.

from math import pi

print(pi)

# Use a comma separted list to import multiple objects. For example:
from math import pi, sqrt

# imports all objects form a module. For example: "from math import *"
# This is generally discouraged, as it confuses variables in your code with
# variables in the external module.



# You can import module or object under a different name using the "as"
# keyword. This is mainly used when a module or object has a long or 
# confusing name.
from math import sqrt as square_root
print(square_root(100))

import math as m
#print(math.sqrt(25))
print(m.sqrt(25))
