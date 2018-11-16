#!/usr/bin/python2
# coding=utf-8

from bs4 import BeautifulSoup

broken_html = '<ul class=country><li>Area<li>Population</ul>'
# parse the html
soup = BeautifulSoup(broken_html, 'html.parser')
fixed_html = soup.prettify()
#print(broken_html)
#print(fixed_html)

ul = soup.find('ul', attrs = {'class':'country'})
print(ul.find('li')) #return just the first match
print(ul.find_all('li')) #return just the first match

import urllib2
def download(url, user_agent='wswp', num_retries=2):
	print 'Downloading:', url
	headers = {'User-agent': user_agent}
	request = urllib2.Request(url, headers=headers)
	#restry 2 times again
	try:
		html = urllib2.urlopen(url).read()
	except urllib2.URLError as e:
		print 'Download error:', e.reason
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				# recursively retry 5xx HTTP errors
				return download(url, num_retries - 1)

	return html

url = 'http://example.webscraping.com/places/default/view/Armenia-12'
html = download(url)
soup = BeautifulSoup(html)
tr = soup.find(attrs={'id':'places_area_row'})
td = tr.findall(attrs={'class':'w2p_fw'})
area = td.text
print area
