### Learnt from : 
# https://learnpythonthehardway.org/book/ex40.html


# For eaample, create a file like this. Call it mystuff.py
# copy the code below in mystuff.py
def apple():
    print "I AM APPLES!"

# this is just a variable
tangerine = "Living reflection of a dream"


# now call it from another file like this: 

import mystuff
print mystuff.apple()
print mystuff.tangerine

# MODULE: 
	# -	a module is a python file (with some code in it, say variables and fun()) that is imported 
	# 	into another file to access the fuctions from the module 
	# -	these variables and fun() can be called using the .(dot) operator.
	# - in simple words, remember a module is like a dict except unlike only key-value pairs a module
	# 	can have a entire code including fuctions and variables accessible using the .(dot) operator
# for instance: 
mystuff['apple'] # get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangerine # same thing, it's just a variable


