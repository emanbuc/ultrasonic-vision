# ===================================================
#--------------- FAKE HARDWARE SETTINGS ------------

#IMPORT FakeRPi to execute script without real sensors
#IMPORT RPI to execute script on Raspberry with REAL
#sensors

#import FakeRPi.GPIO as GPIO  # real hardware sensors
import RPi.GPIO as GPIO #emulated sensors

# ------------------------------------------------
import random
import os 
import time
from time import strftime
from datetime import datetime 

# ==================================================
# --- GLOBAL CONFIG -------
FAKE_HW = False #True for debug in windows | False to run with real sensors
SENSORS= ['HCSR04_001','HCSR04_002'] #List os sensors unique ID
TRIGGER_GPIOS = [23,22] #List of GPIO connect to sensors trigger pin
ECHO_GPIOS = [24,27] #List of GPIO connect to sensors echo pin
MAIN_TRIGGER_GPIO = 26

## =================================================
# --- GLOBAL VARIABLES



# ==================================================
# --- FUNCTIONS ----------
    
def configureGPIO(TRIGGER_GPIOS,ECHO_GPIOS):

    GPIO.setmode(GPIO.BCM)
    
    for triggerGpio in TRIGGER_GPIOS:
        GPIO.setup(triggerGpio,GPIO.OUT)
    
    for echoGpio in ECHO_GPIOS:
        GPIO.setup(echoGpio,GPIO.IN)
    
    #pull down for trigger button   
    GPIO.setup(MAIN_TRIGGER_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    

def createDataFile():
    filename= strftime("%Y%m%d_%H%M%S")+".csv"
    file = open(filename, "w+")
    if os.stat(filename).st_size == 0: 
        sensorIdString = ""        
        for sensorIdex in range(0,len(SENSORS)):
            sensorIdString = sensorIdString + ","+str(SENSORS[sensorIdex])

        file.write("Time"+sensorIdString+ "\n")
    return file

def writeDataToLocalFile(sampleTimestamp,sensorIds,distances):
    distanceString = ""
    for distance in distances:
        distanceString = distanceString+","+str(distance)
    
    file.write(str(sampleTimestamp)+distanceString+"\n")
    file.flush()

def calculateDistance(pulseDuration):
    distance = pulseDuration * 17150
    distance = round(distance, 2)
    print(distance)
    return distance

def readFromSensor(sensorIndex):
    GPIO.output(TRIGGER_GPIOS[sensorIndex], False)
    print ("Waitng For Sensor To Settle. Sensor index: "+str(sensorIndex))
    time.sleep(2)

    GPIO.output(TRIGGER_GPIOS[sensorIndex], True)
    time.sleep(0.00001)                      
    GPIO.output(TRIGGER_GPIOS[sensorIndex], False)                 

    while GPIO.input(ECHO_GPIOS[sensorIndex])==0:               
        pulse_start = time.time()              

    while GPIO.input(ECHO_GPIOS[sensorIndex])==1:               
        pulse_end = time.time()
    
    return pulse_start,pulse_end

def doMeasure():
    print(" ==== doMeasure starts ====")
    distances = []
    for sensorIndex in range(0,len(SENSORS)):
        if FAKE_HW == True:
            pulse_start = time.time()
            pulse_end= pulse_start + ( random.randint(1,100)/10000.0)

        else:
            pulse_start,pulse_end =readFromSensor(sensorIndex)
            time.sleep(0.1) 
                
        pulseDuration = pulse_end - pulse_start
        sampleTimestamp= pulse_end - (pulseDuration/2)
        distance= calculateDistance(pulseDuration)
        distances.append(distance)
    
    writeDataToLocalFile(sampleTimestamp,SENSORS,distances)


# ==================================================
# --- MAIN -----------------------------------------

print("Distance measurement in progress")
print("TRIGGERS: "+ str(TRIGGER_GPIOS))
print("ECHOS: "+str(ECHO_GPIOS))


configureGPIO(TRIGGER_GPIOS,ECHO_GPIOS)
file= createDataFile()

while True:
    if(FAKE_HW):
        mainTriggerState= True
        input("press enter to continue")        
    else:
        mainTriggerState= GPIO.input(MAIN_TRIGGER_GPIO)

    if(mainTriggerState):
        doMeasure()
    else:
        print(".")
# GPIO.cleanup() # Clean up

