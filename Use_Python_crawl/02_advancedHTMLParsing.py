#!/usr/bin/python3
# -*- encoding:utf-8 -*-

url = "http://www.lagou.com"
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen(url)
bs = BeautifulSoup(html, "html.parser")
nameList = bs.findAll()
