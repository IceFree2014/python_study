#!/usr/bin/env python3
# encoding:utf-8

# import libraries
import urllib.request
from bs4 import BeautifulSoup
import time

time_start = time.time()
# specify the url
urlpage = 'https://www.lagou.com/beijing-zhaopin/shujuchanpinjingli/1'
print(urlpage)

# query the website and return the html to variable 'page'
page = urllib.request.urlopen(urlpage)
#print(page.read())

# parse the html using beautiful soup and store in variable 'soup' 
soup = BeautifulSoup(page, 'html.parser')

# find items
s_position_list = soup.find('div', attrs = {'class':'s_position_list'})
item_con_list = s_position_list.find('ul', attrs = {'class':'item_con_list'})
con_list_item_default_list = item_con_list.find_all('li', attrs={'class':'con_list_item default_list'})

# loop over
for item in con_list_item_default_list:
	position_link = item.find('a', attrs={'class':'position_link'}).get('href')
	print(position_link)


time_end = time.time()
print(time_end - time_start)
