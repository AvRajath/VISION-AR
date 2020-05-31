import RPi.GPIO as GPIO
import time
import os

from firebase import firebase


#sensor pin define

touch_on = 26
touch_off = 20

#Our firebase Url where we can update our context status
firebase_url = 'https://ariot-5cdcc.firebaseio.com/'

#Initialize firebase to start communication

#GPIO port init
def init():
         GPIO.setwarnings(False)
         GPIO.setmode(GPIO.BCM)
         GPIO.setup(touch,GPIO.IN,pull_up_down=GPIO.PUD_UP)
         pass


touchstatus = False
#read digital touch sensor
def read_touchsensor():
         global touchstatus
         if (GPIO.input(touch_on)==True): #check for input from ON Touch Sensor
                  touchstatus = True      #Update touch status to True
                  print("ON")
                  context=fb.get("/Context", None)  #get context from context folder on what has been seen
                  if context != "NONE":
                     fb.put("",context,"ON") #update the appliance seen on the database with ON status
                  
         if (GPIO.input(touch_off)==True): #check for input from OFF touch sensor
                  touchstatus = False
                  print("OFF")
                  context=fb.get("/Context", None) #get context from context folder on what has been seen
                  if context != "NONE":
                     fb.put("",context,"OFF") #update the appliance seen on the database with OFF status
         pass
                  

#main loop
def main():
         init()
         print"Please touch"
         print"\n"
         while True:
                  read_touchsensor() #continously read the touch status

if __name__ == '__main__':
         try:
                  main()
                  pass
         except KeyboardInterrupt:
                  pass
         pass
GPIO.cleanup()