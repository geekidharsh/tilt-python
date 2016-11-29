# Modules in python
# 1. Modules: 
		# A module is a file containing Python definitions and statements.
		# As your program gets longer, you may want to split it into several files for easier maintenance. You may also want to use a handy function that you’ve written in 
		# several programs without copying its definition into each program.
		# To support this, Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter.

# File name is the module name with .py at the end. 
# Within a module, the module’s name (as a string) is available as the value of the global variable __name__.

# Let's create a sample module: 
def fib(n):
	results = []
	a,b = 0, 1
	for num in range(a,n):
		b,a = a+b, b
		results.append(b)
	return results
# now if you import this module(i.e modules.py) inside of a python interpreter
# like this:
	# >>> import modules
	# Now call the fib function from the module 
	# >>> modules.fib(10)
	# You will see the following results:
	# [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

	# You can also import this module and specify a name:
	# >>> import modules as fibo
	# >>> fibo.fib(10)
	# >>> [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

	# Or you can directly call the function by calling it in the import 
	# >>> from modules import fib
	# >>> fib(10)
	# [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]