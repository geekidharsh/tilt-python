import pandas as pd

'''
2 kinds of data structures in pandas: 
	1. Series
	2. DataFrames

	Series: 
		Series are 1 dimensional whereas DataFrames are 2 dimensionals. Series are useful for timeseries sort of data. 
'''

# Here we will try a dict with key and values in a list for each key and then put them into ta Series

# create a dict below
url_lists = {'list1': ['www.example.com', 'www.example1.com'], 
			'list2': ['www.exampletwo.com', 'www.examplethree.com']}

# generate Series from the url_lists
test_Series = pd.Series(url_lists)

# Now run these samples to learn more.

# 1. get keys
print test_Series.keys() 
print "----"

# 2. iterate over a certain row in a Series. Say list1
for url in url_lists['list1']:
	print url
print "----"

# 3. iterate over a all data in all rows in a Series
for key in url_lists.keys():
	for url in url_lists[key]:
		print url
print "----"

# 4. write Series into a csv file
test_Series.to_csv('Series-example.csv', encoding='utf-8')
print "----"

# 5. read from a csv into a series
test_Series_reader = pd.Series.from_csv('Series-example.csv')
print test_Series_reader.keys()
print "----"

# 6. a powerful csv reader method is pandas.read_csv(), use that instead for a much general purpose usage
test_Series_reader1 = pd.read_csv('Series-example.csv')
print test_Series_reader1.head()