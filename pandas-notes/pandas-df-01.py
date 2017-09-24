import pandas as pd
import os
import numpy as np
#create a sample dictionary data
web_stats = {'Day': [1,2,3,4,5,6],
			'Visitors':[12,43,23,54,67,23],
			'Bounce_Rate':[65,72,34,21,89,101],
			'Engagement':[5,6,8,9,10,11]}

sampledf = pd.DataFrame(web_stats)

# clears the screen on windows, delete this line if running this script on unix/mac
# os.system('cls')

# prints the sample dataframe. by default pandas prints the dataframe in alphabetical order of Key values
print sampledf 

# Try out these samples firsrt before proceeding down:
# print sampledf.head() #prints first five dataframes only
# print "\n"
# print sampledf.tail() #print last five
# print "\n"
# print sampledf.tail(2) #prints just last two data

print sampledf.set_index('Day')
print sampledf.head() #Notice the Index set earlier is not shown here

# Basically, if you wanted to set the index of the table/dataframe to Day
# Note: Everytime the df is set index like this, the result you see is a new dataframe returned.
# What this means essentially is that the original dataframe copy stays intact, so point to remember.
# In order to set data frame you have to redeclare it like this: 
# sampledf = sampledf.set_index('Day')
# print sampledf.head()

# Now if you want to avoid doing this declaration thing you can do this.
sampledf.set_index('Day', inplace=True)
print sampledf.head()

# To reference as specific column
print sampledf['Visitors']
print "\n\n"

#Another way to reference a specific column, like an attribute
print sampledf.Visitors

# To reference multiple columns
print sampledf[['Bounce_Rate','Visitors']]

#To convert data from a column to a list
print sampledf.Visitors.tolist()
# Note: in python there is no thing as an Array. We have lists and we have multi-dimentional lists


# To convert multiple columns as an array. We can use numpy this way
print np.array(sampledf[['Bounce_Rate','Visitors']])