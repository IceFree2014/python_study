#!/usr/bin/env python3
# -*- encoding:utf-8 -*-


# Scraping the web page using Selenium
# Selenium with geckodriver
# Since we are unable to access the content of the web page using BeautifulSoup,
# we first need to set up a web driver in our python script

# 1.Using selenium with Firefox web driver
# 2.Using a headless browser with phantomJS
# 3.Making an API call using a REST client or Python requests library

# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd

time_start = time.time()
# specify the url
urlpage = 'https://www.lagou.com/beijing-zhaopin/shujuchanpinjingli/'
print(urlpage)

# use headless mode with geckodriver by using the headless option
options = Options()
options.headless = True
#driver = webdriver.Firefox(firefox_options=options, executable_path='your/directory/of/choice')
driver = webdriver.Firefox(options=options)

# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(30)

# find elements by xpath
results = driver.find_elements_by_xpath("//*[@id='componentsContainer']//*[contains(@id, 'listingsContainer')]//*[@class='product active']//*[@class='title productTitle']")
print('Number of result', len(results))

# create empty array to store data
data = []
# loop over results
for result in results:
	product_name = result.text
	link = result.find_element_by_tag_name('a')
	product_link = link.get_attribute("href")
	# append dict to array
	data.append({"product":product_name, "link": product_link})

# close driver
driver.quit()
#print(data)

# save to pandas dataframe
df = pd.DataFrame(data)
print(df)

# write to csv
df.to_csv("asdaYogurtLink.csv")
time_end = time.time()
print(time_end - time_start)

