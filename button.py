import RPi.GPIO as GPIO
import time
from time import sleep
global status

readPin = 14
ledPin = 15
print(GPIO.getmode())
GPIO.setmode(GPIO.BCM)
print(GPIO.getmode())

GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(readPin, GPIO.IN)

status = "off"

try:
	while 1:
		print("current state is " + status)
		if status == "off":
			if GPIO.input(readPin):
				GPIO.output(ledPin, GPIO.HIGH)
				status = "on"
				print("button pressed")
				time.sleep(5)
			continue
		else:
			if GPIO.input(readPin):
				print("initial press")
				time.sleep(2)
				print("just slept")
				if GPIO.input(readPin):
					status = "off"
					print("status " + status)
					print("continued to wait, setting low")
					GPIO.output(ledPin, GPIO.LOW)
					time.sleep(5)
				else:
					print("wasnt held down")
					time.sleep(1)
					print("status " + status)
except KeyboardInterrupt:
	GPIO.output(ledPin, GPIO.LOW)
	GPIO.cleanup()
