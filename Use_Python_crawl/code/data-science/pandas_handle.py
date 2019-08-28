#!/usr/bin/env python
# encoding:utf-8

import pandas as pd

#print(df['职位名称'])
#print(df[1:3])
#print(df.loc[1:3, ['职位名称']])
#print(df[df['公司信息'] == '移动互联网,数据服务'])
#print(df[df['学历'] == '本科及以上 /'])
#print(type(company_infos))
#company_info = company_infos[0]
#print(type(company_info))

filename = 'jobs_lagou_data_science.csv'
filename = 'ba_jobs_lagou.csv'
new_filename = 'add_industry_area_' + filename
df = pd.read_csv(filename)
company_infos = df['公司信息']
strings = "移动互联网,电子商务,金融,企业服务,教育,文化娱乐,游戏,O2O,硬件,社交网络,旅游,医疗健康,生活服务,信息安全,数据服务,广告营销,分类信息,招聘,其他,区块链,人工智能".split(',')

data = []
for company_info in company_infos:
	industry_area = ''
	for string in strings:
		ret = company_info.find(string)
		if ret != -1:
			industry_area += string 
			industry_area +=','
	data.append(industry_area)

# add new column
df['行业领域'] = data

# write to new csv
df.to_csv(new_filename)
