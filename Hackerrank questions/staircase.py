'''
print a staircase of length n that matches with the base size. p
and print something like this. say n is 4 then,
print a ) 
#
##
###
####

print b) 
   #
  ##
 ###
####

'''
import sys

#solution b)
n = int(raw_input("enter the number: "))
for i in range(1,n+1):
	print " "*(n-i)+"#"*i #note: string multiplication works like this A*3 = AAA

for j in xrange(1,n+1):
	print "#"*j