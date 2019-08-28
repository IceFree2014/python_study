#!/usr/bin/env python

import os
import glob
import pandas as pd
import csv

# merge multiple csv file to a file
def merge_multiple_file(path, pattern, new_filename, del_src_file):
	print(os.listdir(path))
	filenames = glob.glob(pattern)
	print(filenames)
	
	# ignore_index =True: clear the existing and reset it in the result by setting the ignore_index Option to True
	new_df = pd.concat([pd.read_csv(filename) for filename in filenames], ignore_index=True)

	# index=False: not add the index	
	new_df.to_csv(new_filename, index=False)
	print(new_df)
	
	if del_src_file:
		for filename in filenames:
			os.remove(filename)
		print(os.listdir("."))

# add header to csv
def add_header_to_csv(pattern):
	filenames = glob.glob(pattern)
	for filename in filenames:
		# to_csv(filename, index=False) index=False: not add index to csv file
		pd.read_csv(filename, names=["职位名称", "招聘部门", "薪资", "地区", "工作经验", "学历", "工作性质", "职位诱惑", "职位描述", "工作地址", "公司信息"]).to_csv(filename, index=False)

#add_header_to_csv(pattern="*_BI_*.csv")
#merge_multiple_file(path=".", pattern="*_BI_*.csv", new_filename="BI.csv", del_src_file=True)

def show_dataFrame_info(filename):
	print("filename: ", filename)
	df = pd.read_csv(filename)
	#print("df type: ", type(df))
	#print("index: ",df.index)
	#print("columns: ", df.columns)
	#print("size: ", df.size)
	#print("values: ", df.values)
	#print("ndim: ", df.ndim)
	#print("axes: ", df.axes)
	print("shape: ", df.shape)

#show_dataFrame_info(filename="BI.csv")

filenames = glob.glob('*.csv')
for filename in filenames:
	show_dataFrame_info(filename)
#merge_multiple_file(path=".", pattern="*data_product_manager*.csv", new_filename="data_product_manager.csv", del_src_file=True)
merge_multiple_file(path=".", pattern="*product_manager*.csv", new_filename="product_manager_20190814.csv", del_src_file=True)
