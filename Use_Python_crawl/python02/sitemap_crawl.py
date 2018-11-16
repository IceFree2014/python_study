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
	# extract the sitemap links
	links = re.findall('<loc>(.*?)</loc>', sitemap)
	#download each link
	for link in links:
		html = download(link)

crawl_sitemap('http://example.webscraping.com/sitemap.xml')
