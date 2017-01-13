import pandas as pd

'''
Code to:
1.	Add a new column with a fixed value to a dataframe from a file using pandas assign()
2. 	Point 1 but with an incoming dataframe, say from an api.
3.	add a new value to a dataframe that depends on some evaluation by taking values from other columns in the dataframe.
4. Merge two dataframes together using pandas append()
'''
# 1. #
yourDF = pd.read_csv(file_name)
yourDF = yourDF.assign(sepal_ratio = 'any_str_value')



# 2. #
# first_response = response['rows']
# first_response = json_normalize(first_response)
# cleaning the data below
# first_response['URL'], first_response['Query'] = first_response['keys'].apply(get_first),first_response['keys'].apply(get_second)        
# first_response.drop('keys', axis=1, inplace=True)
yourDF = yourDF.assign(searchtype = 'any_str_value')


# optionally: 
print yourDF.head()
#store new dataframe to csv file
yourDF.to_csv('outfilename.csv', encoding="utf-8")



# 4. #
df1 = df1.append(df2, ignore_index=True)