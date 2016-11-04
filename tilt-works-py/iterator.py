import os
import sys


def iterator(a, b):
	for x in xrange(1,b):
		a = a + x
	
	print "done"
	return a

print iterator(1,3)