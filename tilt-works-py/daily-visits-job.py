from os import system
#python file in use here : search_analytics_api_visits-date.py
#The python here will pull all the daily visits data and store them in 4 different folders

#clear the screen , this is optional. For unix terminal change 'cls' to 'clear'
#get start and end date
system('clear')
st = raw_input("enter start date in YYYY-MM-DD? ").split()
ed = raw_input("enter end date in YYYY-MM-DD? ").split()
urls = ['http://www.emdmillipore.com', 'https://www.emdmillipore.com','http://www.merckmillipore.com','https://www.merckmillipore.com']

#check start and end date
#checks only for equality, not for: start is less than end date
#compare = cmp(st,ed)
#print compare
#print bin(compare)


## queries data from API and parses into cleaner json format

if st==ed:
	print "Start date and End date should be different. Try again!"

else:
	for url in urls:
            try: 
                param = "python search_analytics_api_visits-date.py "+url+" "+st+" "+ed
                print param
#                system('python search_analytics_api_visits-date.py url st ed')
                print "Finished with :" +url           

            except: 
                print "Failed to complete "+ url


#create a directory for files and folders
#check if the directory already exists and prompt



