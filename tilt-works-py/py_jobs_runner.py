import os
import sys

"""
# Show notification to user for appending the file successfully or show error for failure
# This job runner takes into conisderation that user wants to run just more than one files
# Say you wanted to run a set of python scripts that perform different task for a same set of 
 	command line arguments like start and end date
 	In this case, run a set of python files, 
	python file-1.py st-date ed-date
	python file-2.py st-date ed-date, etc.

# In this case a set of python scripts that:
	1. Take a common command-line/terminal argument, such as 'start date' and 'end date'
	2. Have a commond set of names starting with say "sa_api" and ending with ".py". 
	3. It looks for python script files in this fashion: sa*.py 
	   (for example: sa_api_justanother.py ) in the location it (job-runner.py) resides, 
	   counts all the files found and then takes user input to run them for a date range.
	   perform different tasks,file names as argument
	4. Needless to say,
		It runs at the the files found with the 

"""
def main(location):
	counter = 0 # keep a track of total files found
	files = [] #store the files found at the location
	print "Runner will look for for files here: ", location
	filehead = str(raw_input("Enter the beginning of the file(s) name:").strip())
	print "\nThis runner assumes that all the jobs to run are .py files"

	for file in os.listdir(location):
		try:
			if file.startswith(filehead) and file.endswith(".py"):
				print "Files found:", file
				files.append(str(file))
				counter = counter+1
		except Exception as e:
			raise e
			print "No file found here with given file information."

	print "Total file(s) found with given information: ", counter
	#condition to run the job only if one or more files are found
	if counter==0:
		print "No files to run. Job won't continue"
	else:
		askuser = raw_input	("\nJob will run all these files. Press 1 to continue: ").strip()
		if int(askuser) == 1: # Right now this runner only take an integer as input, to keep things simple.
			print "\nEnter date in this format: YYYY-MM-DD"
			st_date = str(raw_input("Enter the start date: ").strip())
			ed_date = str(raw_input("Enter the end date: ").strip())
		
			if st_date != ed_date:
			    for file in files:
			        try:
			            job = "python "+file+" "+st_date+" "+ed_date
			            print "Now running", job           
			            os.system(job)
			        except:
						print "Error while running file: ", file	
			else:
				print "Start and end dates are wrong. Try again!"
		else:
			print "Job didn't continue"

if __name__ == '__main__':
	main(os.getcwd())