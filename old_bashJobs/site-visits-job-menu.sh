"""
Python files in use are : 
sa_api_example.py

"""

#clear the screen for the job menu
clear 

#store currect directory location
location=$(pwd)
echo "Daily visits data for all sites"
read -p "Enter start date in YYYY-MM-DD: " st
read -p "Enter end date in YYYY-MM-DD: " ed

#check if st and end dates the same
if [ $st == $ed ]
then
   echo "Start date and End date should be different. Try again!"
   exit 0
#run actual program here
else
	echo "Generating results at" $location 
fi

#check if Daily-Visits directory exists, if not create one.
if [ -d $location/Daily-Visits ] 
then 
	mkdir $location/Daily-Visits/daily-visits-$st-$ed

	#store new location in a variable for referencing
	outputlocation = $location/Daily-Visits/daily-visits-$st-$ed
	python sa_api_example.py 'http://www.example.com' $st $ed >> $outputlocation/daily-visits-emd-$st-$ed.txt && echo "Completed with emd" || echo "Failed to pull emd"
else
	echo "Directory Daily-Visits does not exists at: " $location
	mkdir Daily-Visits
	#creating a new location from st and ed dates
	mkdir Daily-Visits/daily-visits-$st-$ed
	echo "Created a new directory at the location"
	echo "Please run the job again! Thanks"
	exit 1
fi

#ask user for more operations else exit the program
echo "Do you want to go ahead and pull daily visits for each device type too"
echo "Select: Y or N"
read userinput

if [ $userinput == 'N' ] 
then
	echo "Bye!"
	exit 2
else
	echo ":::Select from the option below:::"
	echo "desk: Desktop"
	echo "mob : Mobile"
	echo "tab : Tablet"
	#read device selection
	read  sel

	case $sel in
			1 )
			mkdir $outputlocation/$sel/
			python search_analytics_api_visits-desktop.py 'http://www.example.com' $st $ed >> $outputlocation/$sel/$sel-visits-emd-$st-$ed.txt && echo "Completed with"$sel || echo "Failed to pull"$sel
			 	;;
			* )echo "Please enter a valid selection"
	esac
fi


