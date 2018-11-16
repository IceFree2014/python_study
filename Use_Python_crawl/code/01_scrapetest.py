#!/usr/bin/python3
# -*- encoding:utf-8 -*-
url = "https://www.lagou.com/beijing-zhaopin/shujuchanpinjingli/"
url = "http://pythonscraping.com/pages/page1.html"
from urllib.request import urlopen
html = urlopen(url)
print(html.read())
