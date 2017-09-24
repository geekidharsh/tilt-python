# General
# Find the most frequent integer in an array

def frequent_arr(arr):
	temp = []
	count = []
	tempcount = 0
	if len(arr) == 1:
		print "arr has only one item", arr
	else:
		for val in arr:
			temp = val
			tempcount = tempcount + 1
			print
	print temp
	return arr

num_arr = [1,2,4,5,6,7,1,8,9,1,3,1,7]
print frequent_arr(num_arr)

temp
count = []