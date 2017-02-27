# Linked list coded in python

# Quick recap 
# Start pointer to first node
# Node
# Link to next node

###### Singly linked list algorithm: ######

# Traversing a linked list :
'''
Suppose, LIST is a linked list with two linear arrays INFO AND LINK and 
PTR or START is a variable pointin to the current node. 
The current node at the beginning will always point to the first node. 

At each INFO traversal, PTR will point to the next INFO node, such that
1. PTR = LINK[PTR]
2. then process info at the second node like this:
3. INFO[PTR], and again update the PTR node to PTR = LINK[PTR]
4. REPEAT 2,3 until PTR = NULL
[END OF THE LOOP]
'''

# ALGORITHM 

'''
1. SET PTR = START
while PTR != NULL:
	2.	process INFO[PTR]
	3.	SET PTR = LINK[PTR]
'''
