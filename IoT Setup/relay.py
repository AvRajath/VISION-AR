import RPi.GPIO as GPIO
# getting the time libraly
import time

import requests

from firebase import firebase

# setting a current mode
GPIO.setmode(GPIO.BCM)
#removing the warings 
GPIO.setwarnings(False)
#creating a list (array) with the number of GPIO's that we use 
pins = [17,18,27] 

#setting the mode for all pins so all will be switched on 
GPIO.setup(pins, GPIO.OUT)

appservice_url = 'https://testrav.azurewebsites.net/'



while 1:
    fb = requests.get(appservice_url)
    response = fb.json()
    app1=response[0]['status']
    app2=response[1]['status']
    app3=response[2]['status']
    #app4=fb.get("/Appliance-4", None)
    if app1=="ON":
        GPIO.output(pins[0],  GPIO.LOW)
    else:
        GPIO.output(pins[0],  GPIO.HIGH)

    if app2=="ON":
        GPIO.output(pins[1],  GPIO.LOW)

    else:
        GPIO.output(pins[1],  GPIO.HIGH)
        
    if app3=="ON":
        GPIO.output(pins[2],  GPIO.LOW)

    else:
        GPIO.output(pins[2],  GPIO.HIGH)
    





