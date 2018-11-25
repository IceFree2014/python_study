#!/usr/bin/env python3
# encoding:utf-8

# import libraries
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import pandas as pd
import time

# specify the url
urlpage = 'https://www.btime.com/btv/btvws_index'
print(urlpage)

# query the website and return the html to the variable 'page'
page = urlopen(urlpage)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')
# find items
results = soup.find_all('a', attrs={'class':'figure'})
print('Number of results', len(results))

# <a class="figure" results-cid="08da67cea600bf3c78973427bfaba12d" href="/btv/btvws_yst" target="_self" title="养生堂">养生堂</a>
#print(results[0])
#print(type(results[0]))
data = []

# loop over results
for result in results:
	title = result.get('title')
	url = result.get('href')
	des = ''
	btv = 'https://www.btime.com'
	# new url
	url = btv + url
	print(url)
	try:
		page = urlopen(url)
		soup = BeautifulSoup(page, 'html.parser')
		url2 = soup.find_all('a', attrs={'class':'media media-aside'})
		url2 = url2[0].get('href')
		try:
			page = urlopen(url2)
			soup = BeautifulSoup(page, 'html.parser')
			description = soup.find_all('div', attrs={'id':'content-pure'})
			#print(description)
			if description != []:
				description = description[0].getText()
				for string in description:
					des += string.strip()
			else:
				print("description is null")
				des = None
			#print(des)
		except HTTPError:
			print("open url failed,httperror(2)", url2)
			continue
		except URLError:
			print("open url failed, urlerror(2)", url2)
			continue
	except HTTPError:
		print("open url failed,httperror(1)", url)
		#continue
	except URLError:
		print("open url failed, urlerror", url)
		#continue

	data.append({"标题": title, "链接":url, "描述":des})
	time.sleep(0.3)
	#break

# save to pandas dataframe
df = pd.DataFrame(data)
#print(df)

# write to csv
df.to_csv("jiemu_btv.csv")

#print(title)
#print(url)
#print(description)

