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

	return html

import itertools
# note:5次连续下载失败，才会退出程序,避免ID不连续，提前结束
# maximum number of consecutive download errors allowed
max_errors = 5
# current number of consecutive download errors
num_errors = 0
for page in itertools.count(1):
	url = 'http://example.webscraping.com/places/default/view/%d' % page
	html = download(url)
	if html is None:
		# reveived an error tring to downloading this webpage
		num_errors += 1
		if num_errors == max_errors:
			# reached maximum number of
			# consecutive errors so exit	
			break
	else:
		# success -can scrape the the result
		pass

