import RPi.GPIO as GPIO
# getting the time libraly
import time

from firebase import firebase

# setting a current mode
GPIO.setmode(GPIO.BCM)
#removing the warings 
GPIO.setwarnings(False)
#creating a list (array) with the number of GPIO's that we use 
pins = [18,17] 

#setting the mode for all pins so all will be switched on 
GPIO.setup(pins, GPIO.OUT)

firebase_url = 'https://ariot-5cdcc.firebaseio.com/'

fb = firebase.FirebaseApplication(firebase_url, None)

while 1:
	app1=fb.get("/Appliance-1", None)
	app2=fb.get("/Appliance-2", None)
	#app3=fb.get("/Appliance-3", None)
	#app4=fb.get("/Appliance-4", None)
	if app1=="ON":
		GPIO.output(pins[0],  GPIO.HIGH)
	else:
		GPIO.output(pins[0],  GPIO.LOW)

	if app2=="ON":
		GPIO.output(pins[1],  GPIO.HIGH)

	else:
		GPIO.output(pins[1],  GPIO.LOW)