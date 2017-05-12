import flask, flask.views
import os
import utils

class Water(flask.views.MethodView):
	@utils.login_required
	def get(self):
		return flask.render_template('water.html')

	@utils.login_required
	def post(self):
		result = os.system("python /home/pi/flask2/waterServer/startWaterPump.py")
#		result = eval(flask.request.form['expression'])
#		flask.flash(result)
		return flask.redirect(flask.url_for('water'))
