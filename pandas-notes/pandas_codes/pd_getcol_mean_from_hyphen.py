import pandas as pd

# Given a sample input or arrays, obtain mean of the each number at every index, including for hyphen values etc. so 30-34 will become 32
sampleInput = ['12', '13', '14','15','16','17','18','19','20','21','22-23','24-25','26-29','30-34','35-49','50-64','65+']


testdf = pd.DataFrame({'ages': sampleInput, 'times': pd.Timestamp('20160101')}) #times is optional, just playing around.
print testdf.dtypes #to seee all current datatypes. 

'''Elegant way to get mean of all items. 
	How it works: 
	1. str replace replaces all values with'+'
	2. split will split by '-' and expand true returns dataframe exapanding dimensionality.
	3. now that there are two columns or index for each values split by -, use astype to cast a 
	datatype (datatype can be any dataframe or numpy datatype)
	4. finally use pd.DataFrame.mean() to obtain mean of all items in axis 1'''
print testdf['ages'].str.replace('+','').str.split('-', expand=True).astype(float).mean(axis=1)

# optionally, if you want to replace new values to the columns:
testdf['ages'] = testdf['ages'].str.replace('+','').str.split('-', expand=True).astype(float).mean(axis=1)


# alternative method
mean_age = [item.replace('+','') for item in sampleInput]
mean_age = [i.split('-') for i in mean_age]
mean = []
for x in mean_age:
	if len(x) > 1:
		x = int((x[0]+x[1]))/2
		mean.append(x)
print mean




# or you can do this: mean_age = [i.split('-',1)[0] for i in mean_age]
print mean_age