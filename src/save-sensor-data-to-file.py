import RPi.GPIO as GPIO
import random
import os 
import time
from time import strftime
from datetime import datetime 

# ==================================================
# --- GLOBAL CONFIG -------
FAKE_HW = True #True for debug in windows | False to run with real sensors
SENSORS= ['HCSR04_001'] #List os sensors unique ID
TRIGGER_GPIOS = [23] #List of GPIO connect to sensors trigger pin
ECHO_GPIOS = [24] #List of GPIO connect to sensors echo pin

# ==================================================
# --- FUNCTIONS ----------
    
def configureGPIO(TRIGGER_GPIOS,ECHO_GPIOS):

    GPIO.setmode(GPIO.BCM)
    
    for triggerGpio in TRIGGER_GPIOS:
        GPIO.setup(triggerGpio,GPIO.OUT)
    
    for echoGpio in ECHO_GPIOS:
        GPIO.setup(echoGpio,GPIO.IN)

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

def readFromSensor(sensorIndex):
    GPIO.output(TRIGGER_GPIOS[sensorIndex], False)
    print ("Waitng For Sensor To Settle")
    time.sleep(2)

    GPIO.output(TRIGGER_GPIOS[sensorIndex], True)
    time.sleep(0.00001)                      
    GPIO.output(TRIGGER_GPIOS[sensorIndex], False)                 

    while GPIO.input(ECHO_GPIOS[sensorIndex])==0:               
        pulse_start = time.time()              

    while GPIO.input(ECHO_GPIOS[sensorIndex])==1:               
        pulse_end = time.time()
    
    return pulse_start,pulse_end

# ==================================================
# --- MAIN -----------------------------------------

print("Distance measurement in progress")
print("TRIGGERS: "+ str(TRIGGER_GPIOS))
print("ECHOS: "+str(ECHO_GPIOS))


configureGPIO(TRIGGER_GPIOS,ECHO_GPIOS)
file= createDataFile()

#TODO: add start/stop button
while True:
    for sensorIndex in range(0,len(SENSORS)):
        sensorId=SENSORS[sensorIndex] 
        if FAKE_HW == True:
            pulse_start = time.time()
            pulse_end= pulse_start + ( random.randint(1,100)/10000.0)

        else:
            pulse_start,pulse_end =readFromSensor(sensorIndex)
            time.sleep(0.1) 
        
        
        pulseDuration = pulse_end - pulse_start
        sampleTimestamp= pulse_end - (pulseDuration/2)
        distance= calculateDistance(pulseDuration)
        writeDataToLocalFile(sampleTimestamp,sensorId,distance)

