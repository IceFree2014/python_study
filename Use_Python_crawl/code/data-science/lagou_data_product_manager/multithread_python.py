#!/usr/bin/env python3

import _thread
import time

# Define a function for the thread
def print_time(threadName, delay):
	time.sleep(delay)
	print("%s %s" %(threadName, time.ctime(time.time())))

# create two thread as flows
def start_multithreading():
	try:
		for i in range(1, 11):
			string = str(i)
			_thread.start_new_thread(print_time, ("Thread-"+string, 1))
	except:
		print("Error: unable to start thread")

start_multithreading()
while 1:
	pass
