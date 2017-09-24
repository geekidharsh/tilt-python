# 1. Python Class
# Simplest look of a python class is something like this: 
class MyClass:
	# <statements>
	# <statements>
	i = 1.2345
	def f(args):
		return "Hi from f"

	def example(self):
		return "Hello from example"

# Python classes just like any other class feature all functionalities of OOP, 
# syntactically it is similar looking to modula-3 or C++

# 2. Class Objects
# Class objects support two kinds of operations: 
# attribute references and 
# instantiation (basically calling).
# 2.1. Attribute references use the standard syntax used for all attribute references in Python: obj.name.
	# this basically means, Valid attribute names are all the names that were in the class's namespace when 
	# the class object was created.
	# So for example, in above class: 
	# f.MyClass
	# i.MyClass
	# example.MyClass are all valid attribute references
	
	# Additionally, __doc__ is also a valid attribute, returning the docstring belonging to the class: 
	# "this is a sample class".
# 2.2. Class instantiation uses function notation. 
# Just pretend that the class object is a parameterless function that returns a new instance of the class
	x = MyClass() # creates a new instance of the class and assigns this object to the local variable x.
	x.i # this is calling the variable i from MyClass using object x. 

