import mysql.connector
from mysql.connector import errorcode
import db

# try to create a connect request using mysql user and password on the object cnx
# if connection fails throw an exception on err
try:
	cnx = mysql.connector.connect(user='root', password='1234',
                              host='localhost',
                              database='seo_tutorial_database')
	print "\nSuccessfully connected at "+str(cnx)
	cur = db.cursor()
	testdata = cur.execute("SELECT * FROM country_visits_emd_aug2016")
	for rows in testdata:
		print  testdata

except mysql.connector.Error as err:
	print err

else:
	cnx.close()