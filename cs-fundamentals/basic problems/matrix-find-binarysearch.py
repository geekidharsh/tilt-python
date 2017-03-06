# manually iterating over a matrix to find all negative integers
# Find all negative integers in matrix
# Binary search approach
'''
For binary searching to find all negative:
		1. all elements need to be sorted first
		2. use sorted() to sort list in python
'''

square_matrix = [[1,-2,-3], [4,-5,6], [7,-8,9]]

# function to get all items in a 2d matrix aka traversing everything in a matrix and putting it into a 1-d list
def get_mtx_elm(matrix):
	all_elems = []
	if len(matrix) != 0:
		for rows in matrix:
			for elem in rows:
				all_elems.append(elem)
	return all_elems

#search for items in binary search
def find_neg_binarysearch(list):
	first = 0
	last = len(list)-1
	mid = (first+last)/2
	count = 0
	if list[last] < 0: #check if the last element is less than 0 if yes, then return length of entire list since all elements are less than zero
		count = len(list)
	elif list[mid] < 0: 
		count = mid #check if mid elem is less than 0, if yes then return mid since all elements to the left of list[mid] are negative
	else:
		while first<=last:
			# this part is confusing work on it
			if list[mid-1] < 0:
				last = mid - 1
				count = last
			else:
				first = mid+1
	return count



# store all values from matrix in a sorted list
sorted_list = sorted(get_mtx_elm(square_matrix))
print find_neg_binarysearch(sorted_list), sorted_list