""" list """
ls = ['harsh', 'pandey', 'yoyo', 3179992222]
print "\t list"
for item in ls:
	print item

""" tuple """
tpl = ('harsh', 'example', 1234)

print "\t tuple"
for item in tpl:
	print item

""" dict """
keyval = {'1': 'Harsh', '2': 'Pandey', '3': 12312433, '4': ['list', 'in a dict']}

#this iterates all keys only no values
print "\t dict"
for key in keyval:
	print key

# iterate over key and values both
print "\t dict with key, value"
for key, value in keyval.iteritems():
	print "{} has: {}".format(key, value) #this iterates all keys only no values

# create a dict inside a dict
print "\t nested dict"
nested_dict = {'Fruits': ['apple', 'bananas', 'mango'], 'B': {'b.a': 10, 'b.b': 20, 'b.c': ['b', 'c'] } }
for key, value in nested_dict.iteritems():
	print key, value

# dict inside of a dict
print "\nPrint values of a dict inside of a dict", nested_dict['B']

# print values of a dict inside of another dict
for key, value in nested_dict['B'].iteritems():
	print key, value

# Note: 
# 1. Why doesn't python return dict in an order
# 2. Add values to list
# 3. try to change tuples
# 4. add values to keys in dict
# 5. create new key, value pairs in a existing dict
# 6. Add values from a list to a dict