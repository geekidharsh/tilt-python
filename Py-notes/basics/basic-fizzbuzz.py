# 1. swap two numbers without using a a temp variable, hint: use arithmetic operators 
x = int(raw_input("1st\t"))
y = int(raw_input("2nd\t"))	# say x,y = 1,2
x = x+y 					# x becomes 3 
y = x-y						# y becomes 1 i.e initial x.
x = x-y						# x becomes 2 i.e initial y
print "numbers after swapping", x, y


# 2. write a number that prints numbers 1-100 but for multiples of 3 it prints fizz and for 5 it prints buzz, 
	# for number multiples for both 3 and 5 it prints fizzbuzz

for x in xrange(1,100):
	if x%3 == 0:
		if x%5 == 0:
			print "fizzbuzz", x
		else:
			print "fizz", x
	elif x%5 == 0:
		print "buzz", x
