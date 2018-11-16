#!/usr/bin/python
# coding=utf-8

import urllib2
def download(url, user_agent='wswp', num_retries=2):
	print 'Downloading:', url
	headers = {'User-agent': user_agent}
	request = urllib2.Request(url, headers=headers)
	try:
		#html = urllib2.urlopen(url).read()
		html = urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		print 'Download error:', e.reason
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				# recursively retry 5xx HTTP errors
				return download(url, num_retries - 1)

	return html

import re
def crawl_sitemap(url):
	# download the sitemap file
	sitemap = download(url)
	links = re.findall('<td class="w2p_fw">(.*?)</td>', sitemap)[1]
	links = re.findall('<tr id="places_area__row">(.*?)</tr>', sitemap)
	#print type(links)
	print links
	for link in links:
		links = re.findall('<td class="w2p_fw">(.*?)</td>', link)
		print links

crawl_sitemap('http://example.webscraping.com/places/default/view/Aland-Islands-2')
