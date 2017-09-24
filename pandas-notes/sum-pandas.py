import pandas as pd 
import numpy as np

infile = pd.DataFrame.from_csv("all-landing-pages.csv", encoding = "utf-8")
print infile.keys() #get axis names

# DataFrame.count()
# count total rows, pandas counts each rows in each axis.
print infile.count()

# DataFrame.sum()
# sum of all rows that have int or float values. By default looks for all data then sums only int or float type objects/axis
print infile.sum()

# sum of only rows that have int or float values.
print infile.sum(numeric_only=1)