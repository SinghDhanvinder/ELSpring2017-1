import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

def Blink():
  for i in range(0,3):
     print "blink #" + str(+1)
     GPIO.output(17,True)
     time.sleep(.2)
     GPIO.output(17,False)
     time.sleep(.2)

  time.sleep(4.8)
  for i in range(0,4):
    GPIO.output(17,True)
    time.sleep(.2)
    GPIO.output(17,False)
    time.sleep(.2)
  time.sleep(4.8)


try:
  while True:
    Blink()
except KeyboardInterrupt:
    pass
