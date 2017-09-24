#shell job to automate all data pulls
#The python here will pull data and store them in different folders

clear #because it looks better on screen

#python files to run
py_files=(sa_api_file-1.py sa_api_file-2.py)
echo "Note: Please run this file weekly/monthly (To avoid file clutter)"
#use this to pass as an argument to python scripts
read -p "enter start date in YYYY-MM-DD? " st
read -p "enter end date in YYYY-MM-DD? " ed

if [ $st == $ed ]
then
   echo "Start date and End date should be different. Try again!"
   exit 0
else
   for i in ${py_files[@]};
         do
            python $i $st $ed && echo "Completed running $i " || echo "Couldn't finish running $i"
         done
            echo -e "Successfuly finished all jobs."
            echo "============="   
exit 1
fi

