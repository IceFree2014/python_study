# Getting Started
{

## Which libraies do I need?
{

### For Web Scraping there are a few different libraries to consider
{
#### Beautiful Soup
{

##### Inspect the webpage
{
```
	To know which elements that you need to tartget in your python code, 
you need to first inspect the web page.
	You can inspect the page by right clicking on the element of interest
and select inspect. This brings up the HTML code where we can see the element
that each field is contained within.

	Right click on the element you are interested in and select 'Inspect',this
brings up the html elements.

	When inspecting the page it is easy to see a pattern in the html.

```

```
	Side note: Another check that can be done is to check whether a HTTP GET
request is being made on the website which may already return the results as
structed response such as a JSON or XML format. You can check this from within
the "network tab in the inspect tools", often in the XHR tab. Once a page is
refreshed it will display the requests as they are loaded and if the response
contains a formatted structure, it is often easier to make a request using a
REST Client such as "Insomnia" to return the output.
```
}

##### Parse the webpage html using Beautiful Soup 
{
```
	The first step is to import the libraties that you will be using for your
web scraper. We have already talked about BeautifulSoup above, which help us
to handle the html. The next library we are importing is "urllib" which makes
the connection to the webpage. Finally we will be writing the output to a csv
so we also need to import the csv library. As an alternative, the "json" library
could be used here instead.

```
```
	# import libraries
	from bs4 import BeautifuSoup
	import urllib.request
	import csv

```

```
	# specify the url
	urlpage = 'http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/'
	# query the website and return the html to the variable 'page'
	page = urllib.request.urlopen(urlpage)
	# parse the html using beautiful soup and store in variable 'soup'
	soup = BeautifulSoup(page, 'html.parser')
	print(soup)
```
}

##### Search for html elements 
{
```
	soup->find->table:
		As all of the results are contained within a table, we can search the
soup object for the table using the "find" method.
	table->find_all->each row:
		We can then find each row within the table using the "find_all" method.
```
```
	# find results within table
	table = soup.find('table', attrs={'class':'tableSorter'})
	results = table.find_all('tr')
	print('Number of results', len(results))
```

```
	This structure is consistent throughout all rows on the webpage(which may
not always be the case for all websites!),and thereforce we can again use the 
"find_all" method to assign each column to a variable that we can write to a 
csv or JSON by searching for the <td> element.
	results--rows
	data = results.find_all('td')---column
```
}

##### Looping through elements and saving variables 
{
```
	list->append->results->list->file:
		In python, it is useful to append the results to a list to then write the
data to a file. We should declare the list and set the headers of the csv before
the loop with the following:
```
```
	# create and write headers to a list
	rows = []
	rows.append(['Rank', 'Company Name', 'Webpage', 'Description', 'Location',
'Year end', 'Annual Sales rise over 3 years', 'Sales', 'Staff', 'Comments'])
	print(rows)
```
```
	The next step is to loop over the results, process the data and append to
rows which can be written to a csv.
```
```
	# loop over results
	for result in results:
		# find all colums per result
		data = result.find_all('td')
		# check that columns have data
		# Since the first row in the table contains only the headers, we can skip
		# this result, as shown above.
		if len(data) == 0:
			continue
```
```
	# write columns to variables
	rank = data[0].getText()
	company = data[1].getText()
	location = data[2].getText()
	yearend = data[3].getText()
	salesrise = data[4].getText()
	sales = data[5].getText()
	staff = data[6].getText()
	comments = data[7].getText()
```
```
	The above simply gets the text form each of the columns and saves to variables.
Some of this data however needs further cleaning to remove unwanted characters
or extract further information.
```
}

##### Data Cleaning 
{
```
	We would like to split "company" into the company name and the description
whcih we can do in a few lines of code.
```
```
	# extract description from the name
	companyname = data[1].find('span', attrs={'class':'company-name'}).getText()
	description = company.replace(companyname, '')

	# remove unwanted characters
	sales = sales.strip('*').strip('†').replace(',', '')
```
```
	# go to link and extract company website
	url = data[1].find('a').get('href')
	page = urllib.request.urlopen(url)
	# parse the html
	soup = BeautifulSoup(page, 'html.parser')
	# find the last result in the table and get the link
	try:
		tableRow = soup.find('table').find_all('tr')[-1]
		webpage = tableRow.find('a').get('href')
	except:
		webpage = None
```
```
	# write each result to rows
	rows.append([rank, companyname, webpage, description, location, yearend,
salesrise, sales, staff, comments])

print(rows)

```
```
	It is then useful to print the variable outside of the loop, to check that
it looks as you expect before writing it to a file!
```
}

##### Writing to an output file 
{
```
	# Create csv and write rows to output file
	with open('techtrack100.csv', 'w', newline='') as f_output:
		csv_output = csv.writer(f_output)
		csv_output.writerows(rows)
```
}

##### Summary
{
```
	web scraping with python:
		Connecting to a webpage(urllib.request.urlopen)
		Parsing html using BeautifulSoup(soup = Beatifulsoup(page, 'html.parser'))
		Loop through the soup object to find elements(soup.find('table').find_all())
		Performing some simple data cleaning(strip, replace method)
		Writing data to a csv	
```
} 

}

#### Requests

#### Scrapy

#### Selenium
}


}


}
