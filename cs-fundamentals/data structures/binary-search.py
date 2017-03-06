# for binary search you need to have the list sorted already
sample_list = [1,2,5,6,7,8,11,13,15,18,21]

# find all the integers smaller than 15

get_item = int(raw_input("enter item to look up: ").strip())

def binary_search(item, ls):
	first = 0
	last = len(ls)-1 #index of the last item i.e total size of list = 11 so last item's index is list[10]
	mid = (first+last)/2
