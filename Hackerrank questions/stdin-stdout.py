# Question
# Read input from stdin
# s = raw_input("How many chickens does it taketo cross the road?")
# 0>= value <=500

## This is the solution to take a string input into s and compare the string value for the case: 0>= value <=500

s = [input("How many chickens does it take to cross the road?")]
if s[0]>=0 and s[0]<=500:
	print s[0]
else:
	print "Max value is 500"


## This solution that converts s from string to int and then compares it for the test case.

s = int(input("How many chickens does it take to cross the road?"))
if s>=0 and s<=500:
	print s
else:
	print "Max value is 500" 