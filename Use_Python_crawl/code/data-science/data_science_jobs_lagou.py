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
import csv
import pandas as pd

filename = 'jobs_lagou_data_science.csv'

def isEmptyListText(empty_list):
	if empty_list == []:
		return None
	else:
		return empty_list[0].text

def getJobsInfo(urlpage):
	new_driver = webdriver.Firefox()
	# get web page
	new_driver.get(urlpage)
	# execute script to scroll down the page
	new_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
	# sleep for 30s
	time.sleep(30)

	# find elements by xpath
	# [@class='con_list_item default_list'] [@class='position_link']
	job_name = isEmptyListText(new_driver.find_elements_by_xpath("//*[@class='job-name']//*[@class='name']"))
	
	job_company_name = isEmptyListText(new_driver.find_elements_by_xpath("//*[@class='job-name']//*[@class='company']"))
	salary     = isEmptyListText(new_driver.find_elements_by_xpath("//*[@class='job_request']//*[@class='salary']"))
	area       = isEmptyListText(new_driver.find_elements_by_xpath("//*[@class='job_request']/p[1]/span[2]"))
	work_times = isEmptyListText(new_driver.find_elements_by_xpath("//*[@class='job_request']/p[1]/span[3]"))
	education  = isEmptyListText(new_driver.find_elements_by_xpath("//*[@class='job_request']/p[1]/span[4]"))
	work_full_time  = isEmptyListText(new_driver.find_elements_by_xpath("//*[@class='job_request']/p[1]/span[5]"))
	
	try:	
		advantage   = new_driver.find_element_by_class_name('advantage').text
		job_advantage   = new_driver.find_element_by_class_name('job-advantage').text
		job_advantage = job_advantage.replace(advantage, '')
		description   = new_driver.find_element_by_class_name('description').text
		job_description = new_driver.find_element_by_class_name('job_bt').text
		job_description = job_description.replace(description, '')
		mappreview = new_driver.find_element_by_id('mapPreview').text
		job_address = new_driver.find_element_by_class_name('work_addr').text
		job_address = job_address.replace(mappreview, '')
		job_company = new_driver.find_element_by_class_name('job_company').text
	except:
		return
	
	data = []
	# append dict to array
	data.append([job_name, job_company_name, salary, area, work_times, education, work_full_time, job_advantage, job_description, job_address, job_company])

	with open(filename, 'a', newline='') as f_output:
		csv_output = csv.writer(f_output)
		csv_output.writerows(data)

	# close current windows
	new_driver.quit()
	
# use headless mode with geckodriver by using the headless option
options = Options()
options.headless = True
#driver = webdriver.Firefox(options=options)
driver = webdriver.Firefox()

# create empty array to store data
data = []
data.append(["职位名称", "招聘部门", "薪资", "地区", "工作经验", "学历", "工作性质", "职位诱惑", "职位描述", "工作地址", "公司信息"])
# Create csv and write rows to output file
with open(filename, 'w', newline='') as f_output:
	csv_output = csv.writer(f_output)
	csv_output.writerows(data)
#print(data)

# specify the url
for i in range(1, 31):
	i = str(i)
	urlpage = 'https://www.lagou.com/beijing-zhaopin/shujuchanpinjingli/'
	urlpage = urlpage + i
	print(urlpage)

	# get web page
	driver.get(urlpage)
	# execute script to scroll down the page
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
	# sleep for 30s
	time.sleep(1)

	# find elements by xpath
	#results = driver.find_elements_by_xpath("/html/body/div[@id='content-container']/div[@id='main_container']/div[@class='content_left']/div[@id='s_position_list']/ul[@class='item_con_list']/li[@class='con_list_item default_list'][1]/div[@class='list_item_top']/div[@class='position']/div[@class='p_top']/a[@class='position_link']")
	# [@class='con_list_item default_list'] [@class='position_link']
	results = driver.find_elements_by_xpath("//*[@class='con_list_item default_list']//*[@class='position_link']")

	# loop over
	for position_link in results:
		link = position_link.get_attribute('href')
		print(link)
		getJobsInfo(link)

	print("----------------------------------------------------------")
	# close driver
	#driver.close()

# close driver
driver.quit()
