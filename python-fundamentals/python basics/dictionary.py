import time
import sys

#define a dictionary with string keys
def myDict(fn, ln, skype, phone):
	starttime = time.time()
	myInfo = {'firstName': fn, 'lastName': ln , 'skype': skype, 'phone': phone}
	for item in myInfo:
		print myInfo.get(item)
	print (time.time() - starttime)*100 #multiplying time by 100 to get a significant number in sec since actual time is too small
	return myInfo

def myList(fn, ln, skype, phone):
	starttime = time.time()
	myInfo  = [fn, ln, skype, phone]
	for item in myInfo:
		print item
	print (time.time() - starttime)*100
	return myInfo

myDict('harshvardhan', 'pandey', 'harshvardhan.pandey', '317 793 8959')
myList('harshvardhan', 'pandey', 'harshvardhan.pandey', '317 793 8959')
# print myInfo # Access full dictionary here

# print myInfo['phone'] # access a key list by attribute name

# # Add more key value pairs 
# myInfo[1] = 'hello'
# myInfo[2] = 'hi' #add nother key value pair
# print myInfo

# myInfo['firstName'] = 'harsh' #this will overwrite any existing value for that key. In this case key :'firstName'
# print myInfo

# #delete a key\keys with it's item from a dict. 
# del myInfo[1], myInfo[2]
# print myInfo

# # Quick hack to turn all values in the dict into a list
# myInfoList = [myInfo[x] for x in myInfo]
# print myInfoList