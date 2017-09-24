'''
Problem: 
Shashank likes strings in which consecutive characters are different. For example, he likes ABABA, 
while he doesn't like ABAA. Given a string containing characters  and  only, 
he wants to change it into a string he likes. To do this, he is allowed to delete the characters in the string.

Your task is to find the minimum number of required deletions.

-Input Format
The first line contains an integer , i.e. the number of test cases. 
The next  lines contain a string each.

Output Format
For each test case, print the minimum number of deletions required.

Constraints
length of string 

Sample Input

5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB
Sample Output

3
4
0
0
4
'''


testcount = int(raw_input("enter the number of test cases:\t"))
input_arr = []
while len(input_arr) < testcount:
	input_arr.append(raw_input("enter test arrays:\t"))
else:
	print "test input can't be more than test cases specified", len(input_arr)
def swap_arr(arr, a,b):
	temp = A
	
# print "your inputs are",
# for inputs in input_arr:
# 	print inputs
