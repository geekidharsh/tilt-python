# manually iterating over a matrix to find all negative integers
# Find all negative integers in matrix
# linear sorting and searching approach: each and every element is touched once
square_matrix = [[1,-2,-3], [4,-5,6], [7,-8,9]] #square matrix of size 3by3


# function to get all negative integers
def find_neg_num(matrix):
	neg_num = [] # create an empty list to store values later
	for rows in square_matrix:
		for elem in rows:
			if elem < 0:
				neg_num.append(elem)
	return neg_num

negatives = find_neg_num(square_matrix)
print "Total negative integers found: {} and the numbers are: {} ".format(len(negatives), negatives)


''' Alternative solution:
	define two functions: 
		1. to get all elements from a matrix
		2. to find all negative numbers in those elements'''

# function to get all items in a 2d matrix aka traversing everything in a matrix and putting it into a 1-d list
def get_mtx_elm(matrix):
	all_elems = []
	if len(matrix) != 0:
		for rows in matrix:
			for elem in rows:
				all_elems.append(elem)
	return all_elems

# find all negative numbers using get_mtx_elm()
def find_neg(matrix):
	neg_nums = []
	for element in get_mtx_elm(matrix):
		if element < 0:
			neg_nums.append(element)
	return neg_nums

print "found using get elem and find:", find_neg(square_matrix)
