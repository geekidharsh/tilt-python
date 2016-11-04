#	commaseperator.py
import csv
import os
import sys
import pandas as pd

'''
Copy paste this file to any directory of csv files and run it to: 
1. Look all csv files in the location
2. count total number of csvfiles found
3. read all csv files one by one on screen
4. count total rows read. Once all rows are read!
'''

#declaring variables here
location = os.getcwd()
counter = 0 #counter to keep a track of total files found
files = [] #array to keep the files found at the location
countrows = 0 #counter to keep a track of row count
outputfile  = open('testout.csv', "wb")
writer = csv.writer(outputfile, delimiter='\t', quotechar='"')


os.system('cls') #delete this line if running this script on a linux based machine. This line just clears the screen on windows or replace this line with : os.system('clear')
print "\nYour are here: "+str(location)
for file in os.listdir(location):
	if file.endswith(".csv"):
		print "Csv file found:"+file
		files.append(file)
		counter = counter+1

print "\nTotal csv files found at this location: "+str(counter) #display total count of csv files

#read all the csv files present in the location
askuser = raw_input("\nDo you want to read all files csv files. Press 1 for Yes. Press any other key for No: ")
if askuser == '1':
	for csvfiles in files:
		with open(csvfiles) as csvfile:
			try:
				for newline in csvfile:
					countrows = countrows+1
#					writer.writerow(newline)
			except Exception, e:
				print e
else:
	print "\nNo files read!"


print "\nTotal rows read", countrows



'''
# pass file names as argument
# open files in csv and read csv
# read files with 'with' and append them in a new line
# show notification to user for appending the file successfully or show error for failure
# find common headers and remove them
# create final file in csv in the same directory
'''