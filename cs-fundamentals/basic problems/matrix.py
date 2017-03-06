# write a matrix in python 
'''
Tranformation options: Transformation basically means swaping rows with columns in a matrix
	Clockwise transform
	Counter Clockwise transform
	Tranformation with inplace matrix. i.e to transform and replace the existing(or inplace) matrix 

2D matrix
	Square matrix or n by n matrix:
		square matrix is the only type of matrix than can be transformed inplace i.e it can be transformed 
		fully to replace the existing square matrix in place. Since to fully transform inplace we need a matrix of size n

	Rectangular matrix or m by n matrix
'''

# Other usage: 
# 	1. 	traverse through all items in a matrix
# 	2.	traverse from bottom
# 	3.	traverse to find all positive integers / negative integers in a 2d matrix
#	4. 	take values from a function to a new matrix
#	5.	take values from a function or list to an existing matrix

# 2d matrix
	# Square
square_matrix = [[1,-2,-3], [4,-5,6], [7,-8,9]] #square matrix of size 3by3
for items in square_matrix:
	print items


	# Rectangular
rect_matrix = [[12,34,56,78], [90,12,13,15]]
for row in rect_matrix:
	print row

# Transpose a matrix in python
	''' 
	Using zip() function : 
	zip() creates a tuple of x[i] elements of the matrix together and puts them in a list
	'''
trans_square_mtx = zip(*square_matrix)
print trans_square_mtx
