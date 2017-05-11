import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

def Start():
	for i in range(0,3):
		print "watering"
		GPIO.output(17, True)
		time.sleep(1)
		GPIO.output(17, False)
		time.sleep(1)
	GPIO.output(17, True)	
Start()
