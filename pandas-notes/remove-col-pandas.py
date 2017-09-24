import pandas as pd
import os

getData = pd.DataFrame.from_csv("visits-by_searchtype2017-03-012017-04-30.csv")
print getData.head()
get_val = lambda x: x.replace('[', '').replace(']', '') # remove braces from date
getData = getData.drop('startDate', 1)
getData = getData.drop('endDate', 1)
getData['Date'] = getData['Date'].apply(get_val)
print getData.head()
getData.to_csv("visits-by-searchtype-mar-to-apr-2017.csv", encoding="utf-8", ignore_index=True)