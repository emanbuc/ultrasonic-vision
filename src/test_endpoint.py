import requests
import json
from json.decoder import JSONDecoder
import sys, getopt

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://64b32d7c-d926-4197-b807-1350e63adf7c.westeurope.azurecontainer.io/score'

# If the service is authenticated, set the key or token
key = ''

SENSORS= ['HCSR04_001','HCSR04_002','HCSR04_003','HCSR04_004','HCSR04_005','HCSR04_006','HCSR04_007'] #List os sensors unique ID
# Two sets of data to score, so we get two results back
rawData = {"Time": 0}
#EMPTY_SEVEN
rawData['HCSR04_001'] = 54.2
rawData['HCSR04_002'] = 55.0
rawData['HCSR04_003'] = 55.3
rawData['HCSR04_004'] = 53.2
rawData['HCSR04_005'] = 48.9
rawData['HCSR04_006'] = 48.8
rawData['HCSR04_007'] = 49.3
            
          #BENA_CAN
#         {
#             "Time": 0,
#             "HCSR04_001": 20.3,
#             "HCSR04_002": 15.9,
#             "HCSR04_003": 17.9,
#             "HCSR04_004": 19.6,
#             "HCSR04_005": 28.2,
#             "HCSR04_006": 40.6,
#             "HCSR04_007": 92.8
#           }

def makeRequest(scoring_uri,key):
    wsInputData ={'Column2': '0'}
    wsInputData['distanceSumLow'] = rawData['HCSR04_001'] + rawData['HCSR04_002']
    wsInputData['distanceSumHi'] = rawData['HCSR04_003'] + rawData['HCSR04_004']
    wsInputData['differentialDistanceFromRoof65'] = rawData['HCSR04_006'] - rawData['HCSR04_005']
    wsInputData['differentialDistanceFromRoof67'] = rawData['HCSR04_006'] - rawData['HCSR04_007']
    wsInputData['differentialDistanceFromRoof57'] = rawData['HCSR04_005']- rawData['HCSR04_007']
    
    inputDataObj = {
        "data": [wsInputData]
    }
    print("Input data:")
    print(inputDataObj)
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

def main(argv,key,scoring_uri):
   if len(argv)!= 2:
      print("usage: ultrasonic-vision.py <key> <scoring-uri>")
      sys.exit(2)

   key = argv[0]
   scoring_uri = argv[1]
   objectClass= makeRequest(scoring_uri,key)
   print("Output:")
   print("Object Type: "+ objectClass)

if __name__ == "__main__":
   main(sys.argv[1:],key,scoring_uri)



