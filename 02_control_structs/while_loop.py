#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# A while statement is similar, except that it can be run more than once.
# The statements inside it are repeatedly executed,as long as the condition holds. 
# Once it evaluated to False, the next section of code is executed.
i = 1
while i <=5:
	print(i)
	i = i + 1
print("Finished")

# infinite loop
while 1 == 1:
	print("In the loop")
	break;

# break: To end a while loop prematurely, the break statement can be used.
i = 0
while 1 == 1:
	print(i)
	i = i + 1
	if i >= 5:
		print("Breaking")
		break;
print("Finished")

# continue: Another statement that can be used within loops is continue
# Unlike break, continue jumps back to the top of the loop, rather than stopping it
i = 0
while True:
	i = i + 1
	if i == 2:
		print("Skipping 2")
		continue
	if i == 5:
		print("Breaking 5")
		break
	print(i)
print("Finished")
