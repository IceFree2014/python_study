#!/usr/bin/python3
# -*- encoding:utf-8 -*-
url = "https://www.lagou.com/beijing-zhaopin/shujuchanpinjingli/"
url = "http://pythonscraping.com/pages/page1.html"
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen(url)
#print(html.read())
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)

# html->  <html><head>...</head><body>...</body></html>
	# head->  <head><title> A Useful Page</title></head>
		# title-> <title> A Useful Page </title>
	# body-> <body><h1> An Int..</h1><div>Loremip..</div></body>
		# h1-> <h1> An Interesting Title </h1>
		# div-> <div>Lorem Ipsum dolor...</div>
print(bsObj.html.body.h1)
print(bsObj.body.h1)
print(bsObj.html.h1)
