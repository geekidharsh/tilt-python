import sys

#AND gate
def AND(a,b):
	if a == True and b == True:
		return True
	else:
		return False

#Not an AND gate
def NAND(a,b):
	if a == True and b == True:
		return False
	else:
		return True

#OR Gate
def OR(a,b):
	if a == True or b == True:
		return True
	else:
		return False

#Not an OR Gate
def NOR(a,b):
	if a == True or b == True:
		return False
	else:
		return True

#XOR Gate or exclusive OR gate
def XOR(a,b):
	if a != b:
		return True
	else:
		return False

#XNOR Gate is the logical complement of XOR Gate
def XNOR(XOR):
	if XOR == True:
		return False
	else:
		return True

print "AND Gate Table:"
print "A = False, B = False \t", AND(False, False)
print "A = True, B = False \t", AND(True, False)
print "A = False, B = True \t", AND(False, True)
print "A = True, B = True \t", AND(True, True)

print "\nOR Gate Table:"
print "A = False, B = False \t", OR(False, False)
print "A = True, B = False \t", OR(True, False)
print "A = False, B = True \t", OR(False, True)
print "A = True, B = True \t", OR(True, True)

print "\nNAND Gate Table:"
print "A = False, B = False \t", NAND(False, False)
print "A = True, B = False \t", NAND(True, False)
print "A = False, B = True \t", NAND(False, True)
print "A = True, B = True \t", NAND(True, True)

print "\nNOR Gate Table:"
print "A = False, B = False \t", NOR(False, False)
print "A = True, B = False \t", NOR(True, False)
print "A = False, B = True \t", NOR(False, True)
print "A = True, B = True \t", NOR(True, True)

print "\nXOR Gate Table:"
print "A = False, B = False \t", XOR(False, False)
print "A = True, B = False \t", XOR(True, False)
print "A = False, B = True \t", XOR(False, True)
print "A = True, B = True \t", XOR(True, True)

print "\nXNOR Gate Table:"
print "A = False, B = False \t", XNOR(XOR(False, False))
print "A = True, B = False \t", XNOR(XOR(True, False))
print "A = False, B = True \t", XNOR(XOR(False, True))
print "A = True, B = True \t", XNOR(XOR(True, True))

#Creating truth tables using format
tableformat = '{:<10}' * 6

print "\nNAND GATE with format" 
print tableformat.format("A", "False", "B", "True", ":", str(NAND(False, True)))
print tableformat.format("A", "False", "B", "False", ":", str(NAND(False, False)))
print tableformat.format("A", "True", "B", "True", ":", str(NAND(True, True)))
print tableformat.format("A", "True", "B", "False", ":", str(NAND(True, False)))
print bool(1)