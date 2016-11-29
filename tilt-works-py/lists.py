import sys

# Strings and traversing them
x = 'frog'
print x[3] # g

# Lists and traversing them
xx = ['frog', 'dog', 'cat', 'mice']
print xx[3]

# Slicing and sequencing

### Slicing allows us to slice out substrings, sublists, subtules using their index
### Syntax: string/arrayname[start: end+1 : step]

## One way to remeber how slicing works is this: 
## Thing of indices as the edges | in between the characters. 
## The left edge of the first character is numbered 0, 
## and so the right edge of the last character of a string of length n will be n, example:-

# +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1


# Strings are immutable, i.e you cannot assign a new character in an index in a string, that has already been assigned. 
# Note: a character 'c' in computer is really just a smaller string of index 0.

x = 'computer'
print x[:3] #items in index 0 through 2 (i.e. 0, 1, 2)
print x[3:] #items in index 3 through end
print x[:-2] #items in this string except for the last two
print x[-2:] #only the last two items in the string
# print x[0:6:2] in the string


# Concatenating: Misc

### 1. Two or more string literals i.e the ones enclosed in quotes are concatenated automatically
print 'stri' 'ngs'
### 2. Concatenating and repeating using strings + and *
print 3 * 'Hi' + 'Bye!'
### It is possible to join lists by creating a lists containing lists.
a = ['a', 'b', 'c', 'd']
y = ['a1', 'b1', 'c1']
z = [a, y]
print z

a, b = 0, 1
while b<15:
	print b
	a, b = b, a+b