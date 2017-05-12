import flask, flask.views , MySQLdb
import os
import utils

class Chart(flask.views.MethodView):
	@utils.login_required
    	def get(self):

		db = MySQLdb.connect("localhost","logger","password","temperatures" )

       		cursor = db.cursor()

        	sql = "select * from temperaturedata" # where DATE_FORMAT(dateandtime, '%Y-%m-%d') = curdate();"
		
		result1 = ""
		
        	try:
                	cursor.execute(sql)
                	results = cursor.fetchall()
                	for row in results:
                        	dateandtime = row[0]
                        	sensor = row[1]
                        	temperature = row[2]
                        	humidity = row[3]

                        	date = "['%s',%s,%s]" %(dateandtime,temperature,humidity)
                        	result1 = result1 + date + ","


        	except:
                	print "Error: unable to fecth data"
		

        	db.close()
		return flask.render_template('chart.html', result1=result1)
