import flask, flask.views , MySQLdb
import os
import utils

class Temperature(flask.views.MethodView):
	@utils.login_required
    	def get(self):

		db = MySQLdb.connect("localhost","logger","password","temperatures" )

       		cursor = db.cursor()

        	sql = "select * from temperaturedata where DATE_FORMAT(dateandtime, '%Y-%m-%d') = curdate();"
		
		result1 = "<table width=600 border=1 cellpadding=1 cellspacing=1 align=center>"
		result1 = result1 + "<tr>"
		result1 = result1 + "<th>Date</th>"
		result1 = result1 + "<th>Sensor</th>"
		result1 = result1 + "<th>Temperature</th>"
		result1 = result1 + "<th>Humidity</th>"
		result1 = result1 + "</tr>"
		
        	try:
                	cursor.execute(sql)
                	results = cursor.fetchall()
                	for row in results:
                        	dateandtime = row[0]
                        	sensor = row[1]
                        	temperature = row[2]
                        	humidity = row[3]

                        	date = "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" %(dateandtime,sensor,temperature,humidity)
                        	result1 = result1 + date


        	except:
                	print "Error: unable to fecth data"

		result1 = result1 + "</table>"
		#result1 = "hola2"

        	db.close()
		return flask.render_template('temp.html', result1=result1)

