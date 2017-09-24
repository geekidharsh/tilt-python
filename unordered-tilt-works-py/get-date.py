import datetime 
import calendar

# Get the first and last day of the month for query
input_text = raw_input('Enter the year and month : YYYY-MM: ').strip()
date = datetime.datetime(int(input_text.split("-")[0]),int(input_text.split("-")[1]),1).date()
print date
first_day = str(date.replace(day = 1))

#get last day
last_day = str(date.replace(day = calendar.monthrange(date.year, date.month)[1]))

print first_day, last_day
