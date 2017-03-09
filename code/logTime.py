import os
import time
import sqlite3 as mydb
import sys

def logTime():
	xTime = time.strftime('%Y-%m-%d') #this gives us year month and date
	xDate = time.strftime('%H-%M-%S') #this gives us Hour Min and Sec
	list1 = [xTime, xDate]

	con = mydb.connect('testTime.db')
	with con:
		try:
			cur = con.cursor()
			cur.execute('insert into testTime values(?,?)',list1) #writes time and date into dataBase
			print("Time Logged")
		except:
			print("Error!!")

logTime()
