import csv
import os
import sys
import pandas as pd

'''
Copy paste this script file to any directory of csv files and run it to: 
1. Look all files in the location
2. count total number of files found
3. read all csv files one by one on screen
4. count total rows read. Once all rows are read!
'''

# clear user screen based on system type
# detect the system the user is on
# This is optional. 
# Fun fact: more hacks can be performed using this information. 
if sys.platform == "linux" or sys.platform == "linux2":
    # linux
    os.system('clear')
elif sys.platform == "darwin":
    # OS X
        os.system('clear')
elif sys.platform == "win32":
    # Windows.
        os.system('cls')


#declaring variables here
location = os.getcwd()
print "\nYour are here: "+str(location)

counter = 0 # keep a track of total files found
files = [] #store the files found at the location
countrows = 0 #counter to keep a track of row count
filetype = raw_input("Enter just file extension to look up at the location. Say .txt, .csv etc: ").strip()
outputfile  = open('sample-output'+filetype, "wb")
writer = csv.writer(outputfile, delimiter='\t', quotechar='"')



for file in os.listdir(location):
	if file.endswith(".csv"):
		print "%s file found: %s" %(filetype, file)
		files.append(file)
		counter = counter+1
#display total count of files
print "\nTotal %s files found at this location: %d " %(filetype, counter)


#read all files of the given filetype present in the location
askuser = raw_input("\nDo you want to read all %s files. Press 1 for Yes, any other key for No: ").strip(), %filetype 

#if askuser == '1':
# 	for file in files:
# 		with open(file) as csvfile:
# 			try:
# 				for newline in csvfile:
# 					countrows = countrows+1
# #					writer.writerow(newline)
# 			except Exception, e:
# 				print e
# else:
# 	print "\nNo files read!"


# print "\nTotal rows read", countrows



'''
# pass file names as argument
# open files in csv and read csv
# read files with 'with' and append them in a new line
# show notification to user for appending the file successfully or show error for failure
# find common headers and remove them
# create final file in csv in the same directory
'''