# Your local library needs your help! 
# Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). 
# The fee structure is as follows:
# 1. if book is returned on or before the due date: 
# 	no fine
# 2. if book is returned after the due date but withtin the same calendar month and year. 
# 	Fine = 15 * (number of late days)
# 3. if book is returned after the due month but within the same year. 
# 	Fine = 500 * (number of months late)
# 4. if book is returned after the calendar year. 
# 	Fixed fine of 10000. 

# Contraints:
# 1 <= D <= 31
# 1 <= M <= 12
# 1 <= Y <= 3000
# Has to be a valid gregorian calendar date

import sys

print "Enter return date in D/DD M/MM YYYY"
d1,m1,y1 = raw_input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]

print "Enter due date in D/DD M/MM YYYY"
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]


# if (1 <= (y2,y1) <= 3000) and (1 <= (m2,m1) <= 12) and (1 <= (d2,d1) <= 12):
# 	if (y2==y1) or (y2-y1)>=0:
# 		if (m2==m1) or (m2-m1)>=0:
# 			if (d2==d1) or (d2-d1)>=0:
# 				fine = 0
# 				print fine
# 			elif d2<d1:
# 				fine = 15*(d1-d2)
# 				print fine
# 		elif m2<m1:
# 			fine = 500*(m1-m2)
# 			print fine
# 	else:
# 		fine = 10000*(y1-y2)
# 		print fine
# else:
# 	print "Not a valid date format"

if (y2==y1) or ((y2-y1)>=0):
	if (m2==m1) or ((m2-m1)>=0):
		if (d2==d1) or ((d2-d1)>=0):
			fine = 0
			print fine
		elif d2<d1:
			fine = 15*(d1-d2)
			print fine
	elif m2<m1:
		fine = 500*(m1-m2)
		print fine
else:
	fine = 10000*(y1-y2)
	print fine



	