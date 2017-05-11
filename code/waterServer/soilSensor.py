import RPi.GPIO as GPIO # This is the GPIO library we need to use the GPIO pins on the Raspberry Pi
import time # This is the time library, we need this so we can use the sleep function

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

#def Start():
#        for i in range(0,3):
#                print "watering"
#                GPIO.output(17, True)
#                time.sleep(1)
#                GPIO.output(17, False)
#                time.sleep(1)
#        GPIO.cleanup()

def callback():
    GPIO.output(17, True)
    channel = 27
    if GPIO.input(channel):
        print "Moisture Low"
        for i in range(0,3):
                print "watering"
                GPIO.output(17, False)
                time.sleep(1)
		GPIO.output(17, True)
		time.sleep(1)
	GPIO.output(17, True)	
    else:
        print "Moisture High"
#Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that we have our digital output from our sensor connected to
channel = 27
# Set the GPIO pin to an input
GPIO.setup(channel, GPIO.IN)

# This line tells our script to keep an eye on our gpio pin and let us know when the pin goes HIGH or LOW
#	GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
# This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
#	GPIO.add_event_callback(channel, callback)

# This is an infinte loop to keep our script running
while(True):
	time.sleep(5)
	callback()

#or j in range(0,10):
    # This line simply tells our script to wait 0.1 of a second, this is so the script doesnt hog all of the CPU
#callback()
#time.sleep(5)