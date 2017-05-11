import flask, flask.views
from flask import request
import os
import utils
import smtplib
import mimetypes
import email
import email.mime.application
import sys
from time import strftime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Contact(flask.views.MethodView):
        @utils.login_required
        def get(self):
                return flask.render_template('contact.html')

        @utils.login_required
        def post(self):
		result = "From... "+request.form['name']+", "+request.form['email']+", MESSAGE: "+request.form['expression']
		sender='AquaPi.contact@gmail.com'
		receiver='AquaPi.contact@gmail.com'
		msg = email.mime.multipart.MIMEMultipart()
		msg['Subject'] = 'AquaPi Inquiry from '
		msg['From'] = sender
		msg['To'] = receiver
		body=email.mime.Text.MIMEText(result+strftime(",  %Y-%m-%d %H:%M:%S"))
		msg.attach(body)
		s = smtplib.SMTP('smtp.gmail.com:587')
		s.starttls()
		s.login(sender, '@AquaPi9')
		s.sendmail(sender,receiver,msg.as_string())		
#               result = eval(flask.request.form['expression'])
#               flask.flash(result)
                return flask.redirect(flask.url_for('contact'))


