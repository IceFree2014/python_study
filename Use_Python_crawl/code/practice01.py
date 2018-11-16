#!/usr/bin/python3
# -*- encoding:utf-8 -*-

# findAll(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywords)

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "file:///home/luoyadong/websites/everymac/everymac.com/index.html"
html = urlopen(url)
#print(html.read())
bsObj = BeautifulSoup(html, features="lxml")
nameList = bsObj.findAll("div", {"id" : {"contentcenter_4col_1", "contentcenter_4col_2", "contentcenter_4col_3", "contentcenter_4col_4"}})
text = nameList[0].get_text()
print(text)
print(type(text))
print(len(text))
#print(nameList[1].get_text())
#print(nameList[2].get_text())
#print(nameList[3].get_text())


