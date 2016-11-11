# http://www.python-course.eu/python3_for_loop.php

# For loop in python has an optional else, unlike in C, C++
# Python has an Iterator-based for loop semantic only. This kind of a for loop iterates over an enumeration of a set of items

# 1. For loop with break 
# If a break statement has to be executed in the program flow of the for loop, 
# the loop will be exited and the program flow will continue with the first statement following the for loop, if there is any at all. Usually break statements are wrapped into conditional statements, e.g. 
edibles = ["ham", "spam","eggs","nuts"]

for food in edibles:
    if food == "spam":
        print("No more spam please!")
        break
    print("Great, delicious " + food)
else:
    print("I am so glad: No spam!")
print("Finally, I finished stuffing myself")


# 2. For loop with Continue
# Maybe, our disgust with spam is not so high that we want to stop consuming the other food. Now, this calls into play the continue statement. 
# In the following little script we use the continue statement to go on with our list of edibles, when we have encountered a spam item. So continue prevents us from eating spam!
for food in edibles:
    if food == "spam":
        print("No more spam please!")
        continue
    print("Great, delicious " + food)
    # here can be the code for enjoying our food :-)
else:
    print("I am so glad: No spam!")
print("Finally, I finished stuffing myself")

# 3. The range() function
# Built-in function range() is the right function to iterate over a sequence of numbers
# It generates a squence of arithmetic progressions starting form 0 to n-1 in : range(n)
	# Now try this 
range(10)
	# To prduce a list of numbers generated by range we have to cast range with list
list(range(10))
	#You can specify the starting point of a range and end: range(begin, end) eg.
range(4,10)
	#range above will begin from 4 and go all they to one less than end, so (n-1). 