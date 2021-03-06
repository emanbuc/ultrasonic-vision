# ===================================================
#--------------- FAKE HARDWARE SETTINGS ------------

#IMPORT FakeRPi to execute script without real sensors
#IMPORT RPI to execute script on Raspberry with REAL
#sensors

# import FakeRPi.GPIO as GPIO  # real hardware sensors
import RPi.GPIO as GPIO #emulated sensors

# ------------------------------------------------
import random
import os 
import time
from time import strftime
from datetime import datetime 
import requests
import json
from json.decoder import JSONDecoder
import sys, getopt

import pickle

# ==================================================
# --- GLOBAL CONFIG -------
FAKE_HW = False
 #True for debug in windows | False to run with real sensors
SENSORS= ['HCSR04_001','HCSR04_002','HCSR04_003','HCSR04_004','HCSR04_005','HCSR04_006','HCSR04_007'] #List os sensors unique ID
TRIGGER_GPIOS = [23,22,5,2,17,20,14] #List of GPIO connect to sensors trigger pin
ECHO_GPIOS = [24,27,6,3,18,21,15] #List of GPIO connect to sensors echo pin
MAIN_TRIGGER_GPIO = 26

localClassificatorPath = '../models/knn_classificator_model_pickle_outline_removed.pkl'

CONTINUOUS_MODE = True

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

def createDataFile(label):        
    filename= strftime("%Y%m%d_%H%M%S")+label+".csv"
    file = open(filename, "w+")
    if os.stat(filename).st_size == 0: 
        sensorIdString = ""        
        for sensorIdex in range(0,len(SENSORS)):
            sensorIdString = sensorIdString + ","+str(SENSORS[sensorIdex])

        file.write("Time"+sensorIdString+",ObjectClass\n")
    return file

def writeDataToLocalFile(file,sampleTimestamp,sensorIds,distances,objectClass):
    distanceString = ""
    for distance in distances:
        distanceString = distanceString+","+str(distance)
    
    # precision reduced to seconds. An integer value is better for timestand conversion
    secondsUnixEpocTimestamp = round(sampleTimestamp) 
    file.write(str(secondsUnixEpocTimestamp)+distanceString+","+objectClass+"\n")
    file.flush()

def calculateDistance(pulseDuration):
    distance = pulseDuration * 17150
    distance = round(distance, 2)
    return distance

def readFromSensor(sensorIndex):
    GPIO.output(TRIGGER_GPIOS[sensorIndex], False)
    print ("Waitng 2 seconds for sensor to Settle. Sensor: "+SENSORS[sensorIndex])
    time.sleep(2)

    GPIO.output(TRIGGER_GPIOS[sensorIndex], True)
    time.sleep(0.00001)                      
    GPIO.output(TRIGGER_GPIOS[sensorIndex], False)
    
    pulse_start = time.time()  

    while GPIO.input(ECHO_GPIOS[sensorIndex])==0:               
        pulse_start = time.time()              

    pulse_end = time.time()
    while GPIO.input(ECHO_GPIOS[sensorIndex])==1:               
        pulse_end = time.time()
    
    return pulse_start,pulse_end

def doRemoteObjectClassification(SENSORS, distances,key,scoring_uri):
    
    
    rawData={}
    for sensorIndex in range(0,len(SENSORS)):
        sensor = SENSORS[sensorIndex]
        rawData[sensor] = distances[sensorIndex]

    wsInputData ={'Column2': '0'}
    wsInputData['distanceSumLow'] = rawData['HCSR04_001'] + rawData['HCSR04_002']
    wsInputData['distanceSumHi'] = rawData['HCSR04_003'] + rawData['HCSR04_004']
    wsInputData['differentialDistanceFromRoof65'] = rawData['HCSR04_006'] - rawData['HCSR04_005']
    wsInputData['differentialDistanceFromRoof67'] = rawData['HCSR04_006'] - rawData['HCSR04_007']
    wsInputData['differentialDistanceFromRoof57'] = rawData['HCSR04_005']- rawData['HCSR04_007']
    
    inputDataObj = {
        "data": [wsInputData]
    }
    # Convert to JSON string
    inputDataJson = json.dumps(inputDataObj)

    # Set the content type
    headers = {'Content-Type': 'application/json'}
    # If authentication is enabled, set the authorization header
    headers['Authorization'] = f'Bearer {key}'

    # Make the request and display the response
    resp = requests.post(scoring_uri, inputDataJson, headers=headers)
    
    #TODO: parse json result
    respObj = JSONDecoder().decode(resp.json())
    return respObj['result'][0]

def doLocalClassification(distances,local_classificator):
    result= local_classificator.predict(distances)
    return result[0]
    

def loadLocalModel(localClassificatorPath):
    localClassificator= pickle.load(open(localClassificatorPath, 'rb'))
    return localClassificator
    
def doMeasure():
    print(" ==== doMeasure starts ====")
    distances = []
    for sensorIndex in range(0,len(SENSORS)):
        if FAKE_HW == True:
            pulse_start = time.time()
            pulse_end= pulse_start + ( random.randint(1,100)/10000.0)
            time.sleep(1)

        else:
            pulse_start,pulse_end =readFromSensor(sensorIndex)
            time.sleep(0.5) 
                
        pulseDuration = pulse_end - pulse_start
        sampleTimestamp= pulse_end - (pulseDuration/2)
        distance= calculateDistance(pulseDuration)
        print(distance)
        distances.append(distance)
    return distances,sampleTimestamp

# ==================================================
# --- MAIN -----------------------------------------
def main(argv):
    print("Distance measurement in progress")
    print("TRIGGERS: "+ str(TRIGGER_GPIOS))
    print("ECHOS: "+str(ECHO_GPIOS))
    #readArgument(argv,key,scoring_uri)
    if len(argv)< 3:
        print("usage: ultrasonic-vision.py <key> <scoring-uri> [<training-label>]")
        sys.exit(2)

    key = argv[0]
    scoring_uri = argv[1]
    
    if len(argv)== 3:
        trainingMode = True
        trainingLabel = argv[2]
    


    configureGPIO(TRIGGER_GPIOS,ECHO_GPIOS)
    localClassificator= loadLocalModel(localClassificatorPath)
    
    label=""
    if(trainingMode==True):
        label = "_TRAIN_"+trainingLabel
        
    file = createDataFile(label)

    while True:
        if(FAKE_HW):
            mainTriggerState= True       
        else:
            mainTriggerState= GPIO.input(MAIN_TRIGGER_GPIO)

        if(mainTriggerState):
            distances,sampleTimestamp = doMeasure()
            if(trainingMode==True):
                objectClass= trainingLabel
            else:
                objectClass = doRemoteObjectClassification(SENSORS,distances,key,scoring_uri)
                print("Remote classificator object type: "+ objectClass)
                objectClass = doLocalClassification(distances,localClassificator)
                print("Remote classificator object type: "+ objectClass)
                
            writeDataToLocalFile(file,sampleTimestamp,SENSORS,distances,objectClass)

        else:
            time.sleep(0.1) 
            print(".")

if __name__ == "__main__":
   main(sys.argv[1:])


