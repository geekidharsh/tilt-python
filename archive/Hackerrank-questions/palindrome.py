# write a palindrome program that takes input from user
# writes back the answer if the number is palindrome or not
inp = raw_input("Enter your number to check ")
def palindrome(inp):
	m = int(inp) # say 123
	a = 0
	while m!=0: 
		a = a*10 + m%10 # 3 + 0*10 = 3 
		m = m/10 # 12
	return a #321
if int(inp) == palindrome(inp):
	print "palindrome"
else:
	print "not a palindrome"