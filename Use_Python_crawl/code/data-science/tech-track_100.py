#!/usr/bin/env python3

# import libraries
from bs4 import BeautifulSoup
import urllib.request
import csv

# specify the url
urlpage  = 'http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/'

# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# print(soup)

# find results winthin table
table = soup.find('table', attrs={'class':'tableSorter'})
results = table.find_all('tr')
print('Number of results', len(results))

# the head of the table title
# eight elements 
#<tr>
#<th>Rank</th>
#<th>Company</th>
#<th class="">Location</th>
#<th class="no-word-wrap">Year end</th>
#<th class="" style="text-align:right;">Annual sales rise over 3 years</th>
#<th class="" style="text-align:right;">Latest sales £000s</th>
#<th class="" style="text-align:right;">Staff</th>
#<th class="">Comment</th>
#<!--				<th>FYE</th>-->
#</tr>
#
# print(results[0])

# the first elements of the table (eight elements)
# <tr>
# <td>1</td>
# <td><a href="http://www.fasttrack.co.uk/company_profile/plan-com/"><span class="company-name">Plan.com</span></a>Communications provider</td>
# <td>Isle of Man</td>
# <td>Sep-17</td>
# <td style="text-align:right;">364.38%</td>
# <td style="text-align:right;">*35,418</td>
# <td style="text-align:right;">90</td>
# <td>About 650 partners use its telecoms platform to support more than 100,000 UK business customers</td>
# <!--						<td>Sep-17</td>-->
# </tr>
# print(results[1])

#<tr>
#<td>2</td>
#<td><a href="http://www.fasttrack.co.uk/company_profile/psioxus-2/"><span class="company-name">PsiOxus</span></a>Biotechnology developer</td>
#<td>Oxfordshire</td>
#<td>Dec-17</td>
#<td style="text-align:right;">311.67%</td>
#<td style="text-align:right;">53,136</td>
#<td style="text-align:right;">54</td>
#<td>Received a $15m milestone payment from its development partner Bristol-Myers Squibb in December</td>
#<!--						<td>Dec-17</td>-->
#</tr>
# print(results[2])

# create and write headers to a list
rows = []
rows.append(['Rank', 'Company Name', 'Webpage', 'Description', 'Location', 'Year end', 'Annual sales rise over 3 years', 'Latest sales £000s', 'Staff', 'Comment'])
print(rows)

# loop over results
for result in results:
	# find all columns per result
	data = result.find_all('td')
	# check that columns have data
	if len(data) == 0:
		continue
	# write columns to variables
	rank = data[0].getText()
	company = data[1].getText()
	# extract description from the name
	companyname = data[1].find('span', attrs={'class':'company-name'}).getText()
	description = company.replace(companyname, '')

	# go to link and extract company website
	# ToDo try/except version
	url = data[1].find('a').get('href')
	page = urllib.request.urlopen(url)
	# parse the html
	soup = BeautifulSoup(page, 'html.parser')
	# find the last result in the table and get the link
	try:
		tableRow = soup.find('table').find_all('tr')[-1]
		webpage  = tableRow.find('a').get('href')
	except:
		webpage = None

	location = data[2].getText()
	yearend = data[3].getText()
	salesrise = data[4].getText()
	# remove unwanted characters
	sales  = data[5].getText()
	sales = sales.strip('*').strip('†').replace(',','')
	staff = data[6].getText()
	comments = data[7].getText()

	# write each result to rows
	rows.append([rank, companyname, webpage, description, location, yearend, salesrise, sales, staff, comments])
	#print(rows)
	break

# Create csv and write rows to output file
with open('techtrack100.csv', 'w', newline='') as f_output:
	csv_output = csv.writer(f_output)
	csv_output.writerows(rows)
