import time
import os
import sys
import pandas as pd

'''
looks files and merges them togeth
'''
def main(location):
	start_time = time.time()
	counter = 0 # keep a track of total files found
	files = [] #store the files found at the location
	final_data = pd.DataFrame()
	print "Looking for files here:\t", location
	
	for file in os.listdir(location):
		try:
			if file.endswith(".csv"):
				files.append(str(file))
				thisDF = pd.read_csv(file)
				# extract site, type date info from file name
				file = file.replace(".csv", "").replace("___", "__").replace("__", "://").replace("_s", " ")	# sites = file[:-16].replace("__", "://").replace("_", " ")
				getfileInfo = file.split()
				splitInfo  = getfileInfo[0].replace("_", " ").split()
				thisDF = thisDF.assign(site = splitInfo[0])
				thisDF = thisDF.assign(searchType = splitInfo[1])
				# thisDF = thisDF.assign(site = splitInfo[0])
				final_data = final_data.append(thisDF, ignore_index=True)
				counter = counter+1
		except Exception as e:
			print "No .csv files here. Make sure you have files at the location"
	
	file_loc = location+"/"+"Page_Query-merge-test"
	if (os.path.exists(file_loc)): 
		print "Desitnation Location exists. New file will be created in the location"
	else: 
		os.mkdir(file_loc)
	file_name = file_loc+"/"+"page-query-merged"+str(start_time)+".csv"
	filecount = 0
  	final_data.to_csv(file_name, encoding="utf-8")
  	filecount = filecount+1
  	print "\n"+str(filecount)+" new files page-query files generated at the location."
  	print "Total files found, scanned and merged", counter


if __name__ == '__main__':
	main(os.getcwd())