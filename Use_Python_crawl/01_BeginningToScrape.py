#!/usr/bin/python3
# -*- encoding:utf-8 -*-

url = "http://www.lagou.com"
# version0
from urllib.request import urlopen
html = urlopen(url)
#print(html.read())


# version1
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen(url)
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)


# version2
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
try:
	html = urlopen(url)	
except HTTPError as e:
	print("The server returned an HTTP error")
except URLError as e:
	print("The server could not be found!")
else:
	#print(html.read())
	pass

# version3
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read(), "lxml")
		title = bsObj.body.h1
	except AttributeError as e:
		return None
	return title

title = getTitle(url)
if title == None:
	print("Title could not be found")	
else:
	print(title)

