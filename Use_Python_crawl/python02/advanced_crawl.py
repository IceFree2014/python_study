#!/usr/bin/python
# coding=utf-8

import urllib2
import os
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

def download_with_proxy(url, user_agent='wswp', proxy=None,  num_retries=2):
	print 'Downloading:', url
	headers = {'User-agent': user_agent}
	request = urllib2.Request(url, headers=headers)

	# for proxy
	opener = urllib2.build_opener()
	if proxy:
		proxy_params = {urlparse.urlparse(url).scheme: proxy}
		opener.add_handler(urllib2.ProxyHandler(proxy_params))

	#restry 2 times again
	try:
		#html = urllib2.urlopen(url).read()
		html = urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		print 'Download error:', e.reason
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				# recursively retry 5xx HTTP errors
				return download(url, user_agent, proxy, num_retries - 1)

	return html

import robotparser
def get_robots(url):
    """Initialize robots parser for this domain
    """
    rp = robotparser.RobotFileParser()
    rp.set_url(urlparse.urljoin(url, '/robots.txt'))
    rp.read()
    return rp

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
def link_crawler(seed_url, link_regex, user_agent, max_depth=2):
	crawl_queue = [seed_url] # create a queue (list) and init with seed_url
	#print type(crawl_queue)//list

	#keep track which URL's have seen beforce
	seen = set(crawl_queue)
	#print type(seen)//set

	# depth
	#max_depth = 2
	#depth = seen[url]
	#if depth != max_depth:
	rp = get_robots(seed_url)

	while crawl_queue:
		url = crawl_queue.pop()# pop url form the queue
		#print url
		#print type(url)//str

		# check url passes robots.txt restrictions
		if rp.can_fetch(user_agent, url):
			html = download(url, user_agent)
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
		else:
			print 'Blocked by robots.txt', url

link_crawler('http://example.webscraping.com', '/places/default/(index|view)/', 'BadCrawler')
link_crawler('http://example.webscraping.com', '/places/default/(index|view)/', 'GoodCrawler')


