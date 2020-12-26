import RPi.GPIO as GPIO
import os 
import time
from time import strftime
from datetime import datetime 
    
def configureGPIO(TRIG_01,ECHO_01):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG_01,GPIO.OUT)
    GPIO.setup(ECHO_01,GPIO.IN)

def createDataFile():
    filename= strftime("%Y%m%d_%H%M%S")+".csv"
    file = open(filename, "w+")
    if os.stat(filename).st_size == 0: 
        file.write("Time,SensorId,Value\n")
    return file

def writeDataToLocalFile(sampleTimestamp,sensorId,distance):
      file.write(str(sampleTimestamp)+","+sensorId+","+str(distance)+"\n")
      file.flush()

def calculateDistance(pulseDuration):
    distance = pulseDuration * 17150
    print(distance)
    distance = round(distance, 2)
    return distance
    

TRIG_01 = 23 
ECHO_01 = 24

print("Distance measurement in progress")
print("TRIG_01: "+ str(TRIG_01))
print("ECHO_01: "+str(ECHO_01))


configureGPIO(TRIG_01,ECHO_01)
file= createDataFile()

while True:

  sensorId='HCSR04_001'
  GPIO.output(TRIG_01, False)
  print ("Waitng For Sensor To Settle")
  time.sleep(2)

  GPIO.output(TRIG_01, True)
  time.sleep(0.00001)                      
  GPIO.output(TRIG_01, False)                 

  while GPIO.input(ECHO_01)==0:               
    pulse_start = time.time()              

  while GPIO.input(ECHO_01)==1:               
    pulse_end = time.time()                

  pulseDuration = pulse_end - pulse_start
  sampleTimestamp= pulse_end - (pulseDuration/2)
  distance= calculateDistance(pulseDuration)
  writeDataToLocalFile(sampleTimestamp,sensorId,distance)

