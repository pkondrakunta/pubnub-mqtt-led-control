import RPi.GPIO as GPIO
import time
from pubnub import Pubnub
pubnub= Pubnub(publish_key='demo',subscribe_key='subscribe_key')
def callback(message,channel):
	print (message)
	GPIO.setmode(GPIO.BCM)
 	GPIO.setup(11,GPIO.OUT)
	if (message=="on"):
   	 GPIO.output(11,GPIO.HIGH)
 	if (message=="off"):
  	  GPIO.output(11,GPIO.LOW)

 

def error(message):
 	print ("ERROR : " +str(message))

pubnub.subscribe(channels="my_channel", callback=callback,error=error)
