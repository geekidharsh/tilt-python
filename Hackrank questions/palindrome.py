# write a palindrome program that takes input from user
# writes back the answer if the number is palindrome or not
from os import system


system('clear')
print "Check for palindrome"

inputuser = raw_input("Enter your number to check ")

def palindrome(word):
	check = []
	for c in word[::-1]:
		print check.join(c)
