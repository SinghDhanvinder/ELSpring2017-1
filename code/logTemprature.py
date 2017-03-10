# 10 minutes at 30 seconds temprature get read and then data is sent to a sqlite database.
import os
import time
import sqlite3 as mydb
import sys


# Returns the current time, temperature in Fahrenheit, and temperature in Celsius
def readTemp():
	tempfile = open("/sys/bus/w1/devices/28-000006961c7b/w1_slave")
	tempfile_text = tempfile.read()
	currentTime = time.strftime('%x %X %Z')# Reads time.
	tempfile.close()
	tempC = float(tempfile_text.split("\n")[1].split("t=")[1])/1000 #temp in calcus
	tempF = tempC*9.0/5.0+32.0
	return [currentTime, tempC, tempF]

# Calls the readTemp() and logs temperature. this will give the time to the temprature in sqlite db.
def logTemp():
	con = mydb.connect('temperature.db')
	with con:
		try:
			[t,C,F] = readTemp()
			print "Current temperature is: %s F" %F
			cur = con.cursor()
			sql = "insert into temperatureTable values(?,?,?)"
			cur.execute('insert into temperatureTable values(?,?,?)',(t,C,F))
			print "Temperature logged"
		except:
			print "Error!!"

# every 30 seconds for 10 minutes function gets executed 
def logActivity():
	x = 0;
	while(x<20):
		logTemp()
		time.sleep(30)
		x = x + 1

logActivity()
