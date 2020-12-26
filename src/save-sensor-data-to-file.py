import RPi.GPIO as GPIO
import os 
import time
from time import strftime
from datetime import datetime 

GPIO.setmode(GPIO.BCM) 

TRIG = 23 
ECHO = 24

print("Distance measurement in progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

filename= strftime("%Y%m%d_%H%M%S")+".csv"
file = open(filename, "w+")
if os.stat(filename).st_size == 0: 
        file.write("Time,SensorId,Value\n") 


while True:

  
  GPIO.output(TRIG, False)
  print ("Waitng For Sensor To Settle")
  time.sleep(2)

  GPIO.output(TRIG, True)
  time.sleep(0.00001)                      
  GPIO.output(TRIG, False)                 

  while GPIO.input(ECHO)==0:               
    pulse_start = time.time()              

  while GPIO.input(ECHO)==1:               
    pulse_end = time.time()                

  sensorId='HCSR04_001'
  pulse_duration = pulse_end - pulse_start
  sample_timestamp= pulse_end- (pulse_duration/2)

  distance = pulse_duration * 17150
  print(distance)

  distance = round(distance, 2)
  file.write(str(sample_timestamp)+","+sensorId+","+str(distance)+"\n")
  file.flush() 

