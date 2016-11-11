import os
import sys

'''
# show notification to user for appending the file successfully or show error for failure
# This job runner takes into conisderation that user wants to run just more than one files
# in this case a set of python scripts that :
1. Take a common command-line/terminal argument, such as 'start date' and 'end date'
2. Have a commond set of names starting with say "sa_api" and ending with ".py". 
3. It looks for python script files in this fashion: sa*.py 
   (for example: sa_api_justanother.py ) in the location it (job-runner.py) resides, 
   counts all the files found and then takes user input to run them for a date range.
   perform different tasks,file names as argument
4. Needless to say. 

'''
def main(location):
	counter = 0 # keep a track of total files found
	files = [] #store the files found at the location
	print "\nRunner looked for files here: ", location
	filehead = str(raw_input("Enter the beginning of the file(s) name:").strip())
	print "This runner assumes that all the jobs to run are .py files"

	for file in os.listdir(location):
		try:
			if file.startswith(filehead) and file.endswith(".py"):
				print "Files found:", file
				files.append(str(file))
				counter = counter+1
		except Exception as e:
			raise e
			print "No file found here with given file information."

	print "Total file(s) found with given information:", counter
# Right now this runner only take an integer as input, to keep things simple.
	askuser = raw_input	("\nJob will run all these files. Press 1 to continue: ").strip()
	
	if int(askuser) == 1:
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