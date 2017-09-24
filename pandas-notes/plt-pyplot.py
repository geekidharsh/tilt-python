import matplotlib.pyplot as plt 

	'''matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB. 
	Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, 
	plots some lines in a plotting area, decorates the plot with labels, etc.
	Source: matplotlib.org'''

# 1. 
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
	'''x-axis is generated atuomatically. matplotlib assistes when a [single array is provided] that it is a sequence 
		of y valeus.'''
# 2. 
plt.plot([1,2,3,4], [8,10,12,14])
plt.axis([0,6,0,20])
plt.show()