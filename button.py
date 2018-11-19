#Noah Niedzwiecki | 2018 Nov. 15
#Must have RPi.GPIO installed to run
#This code is meant for a raspberry pi running python v-2.7 or higher

import RPi.GPIO as GPIO
import time
from time import sleep
global status

readPin = 14
ledPin = 15
print(GPIO.getmode())
GPIO.setmode(GPIO.BCM)


GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(readPin, GPIO.IN)

status = "off"

try:
	while 1:
		
		if status == "off":
			if GPIO.input(readPin):
				GPIO.output(ledPin, GPIO.HIGH)
				status = "on"
				
				time.sleep(5)
			continue
		else:
			if GPIO.input(readPin):
				
				time.sleep(2)
				
				if GPIO.input(readPin):
					status = "off"
					
					
					GPIO.output(ledPin, GPIO.LOW)
					time.sleep(5)
				else:
					
					time.sleep(1)
					
except KeyboardInterrupt:
	GPIO.output(ledPin, GPIO.LOW)
	GPIO.cleanup()
