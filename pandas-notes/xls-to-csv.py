import csv
import sys
import os
import pandas as pd
from xlrd import open_workbook

## global variables ##
out_files = [] #output files here

def main(dir_loc):
	dir_items = os.listdir(dir_loc)
	files_found = [] #input file here
	for file in dir_items:
		try:
			if file.endswith(".xls") or file.endswith(".xlsx"):
				print "Files found:", file
				files_found.append(str(file))
		except Exception as e:
			raise e
			print "No .xls files found here."
	print "Total files found:\t", len(files_found)
	print "Do you want to convert all the excel files to .csv:\t"
	take_response = str(raw_input("Say 'y' or 'n':\t").strip())
	if take_response == 'y':
		read(files_found)
	else:
		print "No files will be read!"

def read(files):
	# def file_lookup():
	for file in files:
		try:
			wb = open_workbook(file)
			for sheets in wb.sheets():
				# to read data by sheet : use wb.sheet_by_index(0) , change index value to open a different sheet. starting value is 0 
				rows, col = sheets.nrows, sheets.ncols
				for row, column in range(0,col):
					print sheets.cell_value(column)
		except Exception as e:
			raise
		finally:
			pass

if __name__ == '__main__':
	main(os.getcwd())