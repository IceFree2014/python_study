#!/usr/bin/python3
# -*- encoding:utf-8 -*-

# findAll(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywords)

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/warandpeace.html"
html = urlopen(url)
bsObj = BeautifulSoup(html)

# tag attributes
nameList = bsObj.findAll("span", {"class":"green"})

# multiple tags 
hList = bsObj.findAll({"h1", "h2", "h3", "h4", "h5", "h6"})

# a single tag multiple attributes
rgNameList = bsObj.findAll("span", {"class":{"green", "red"}})

# text parm
nameList = bsObj.findAll(text="the prince")

# keywords
allText = bsObj.findAll(id="text")
# tag attributes
allText = bsObj.findAll("", {"id": "text"})
#allText = bsObj.findAll(class="green")

#print(rgNameList)
print(hList)
print(nameList)
print(len(nameList))
print(allText[0].get_text())
#print(allText[1].get_text())
print(type(allText))
for name in nameList:
	#print(name)
	#print(name.get_text())
	pass


