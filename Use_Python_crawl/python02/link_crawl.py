#!/usr/bin/python
# coding=utf-8

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
	#f = open(url, 'w');
	#f.write(html)
	#f.close()

	return html


import re
def get_links(html):
	"""Return a list of links form html
	"""
	# a regular expression to extract all links form the webpage
	webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
	#print 'webpage_regex', webpage_regex.findall(html)
	# list of all links form the webpage
	return webpage_regex.findall(html)

import urlparse
import time
def link_crawler(seed_url, link_regex):
	crawl_queue = [seed_url] # create a queue (list) and init with seed_url
	#print type(crawl_queue)//list

	#keep track which URL's have seen beforce
	seen = set(crawl_queue)
	#print type(seen)//set

	while crawl_queue:
		url = crawl_queue.pop()# pop url form the queue
		print url
		#print type(url)//str

		html = download(url)
		#print type(html)
		#print html

		#print 'get_links', get_links(html)
		for link in get_links(html):
			time.sleep(0.1)# delay 0.1s
			# check if link matches expected regex
			if re.match(link_regex, link):
				link = urlparse.urljoin(seed_url, link)
				#print 'lyd link', link
				if link not in seen:
					seen.add(link) # avoid again and again download
					crawl_queue.append(link)# add to the queue for download
			else:
				#print "match failed"
				pass

link_crawler('http://example.webscraping.com', '/places/default/(index|view)/')


