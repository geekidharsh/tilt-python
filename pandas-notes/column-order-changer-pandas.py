import pandas as pd
import time
import os
import sys

# looking files
##################################
def main():
	location = os.getcwd()
	start_time = time.time()
	counter = 0 # keep a track of total files found
	frames = pd.DataFrame()
	print "\nYou are here: \t", location
	inp_file =  str(raw_input("Enter .csv file:"))  #store the files found at the location

	if inp_file.endswith(".csv"):
		thisDF = pd.read_csv(inp_file).drop(['Unnamed: 0'],axis=1)
		old_col_order = thisDF.columns.tolist()		#get columns of this data in a list
		print "Old column order:\n", old_col_order
		new_col_order = old_col_order[:-2] 
		new_col_order.append(old_col_order[old_col_order.index('startDate')])
		new_col_order.append(old_col_order[old_col_order.index('site')])
		print "New order:\n", new_col_order
		thisDF = thisDF[new_col_order]
		out_file = 	"new-col-order"+inp_file	
		thisDF.to_csv(out_file)
		print "Column order changed and new file created: ", out_file		
	else: 
		print "This is not a .csv file. Enter valid file name"

if __name__ == '__main__':
	main()