#!/usr/bin/python3
# -*- encoding:utf-8 -*-
url = "https://www.lagou.com/beijing-zhaopin/shujuchanpinjingli/"
url = "http://pythonscraping.com/pages/page1.html"

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None	
	try:		
		bsObj = BeautifulSoup(html.read())
		title = bsObj.body.h1
	except AttributeError as e:
		return None	

	return title

url = "http://pythonscraping.com/pages/page1.html"
title = getTitle(url)
if title == None:
	print("Title could not be found")
else:
	print(title)


