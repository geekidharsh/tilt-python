#!/usr/bin/python

# printing command line arguments in python
# run this file as python cmdlineargs.py 'abcdefg'
# sys.argv will store the command line arguments passed in python while running from terminal
# sys.argv stores all cmd line args in a list. 
# sys.argv[0] is the first argument passed, which is basically the filename

import sys
Arglen = int(len(sys.argv))
arguments = sys.argv

for argument in arguments:
	if Arglen >1:
		print argument
	else:
		print "No command line arguments passed"

#print total number of arguments
print "\nTotal arguments: ",Arglen
print "This file name: "+str(arguments[0]) #checking the file name


