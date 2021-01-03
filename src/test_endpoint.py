import requests
import json
import sys, getopt

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://64b32d7c-d926-4197-b807-1350e63adf7c.westeurope.azurecontainer.io/score'

# If the service is authenticated, set the key or token
key = ''

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            "Time": 0,
            "HCSR04_001": 20,
            "HCSR04_002": 20,
            "HCSR04_003": 20,
            "HCSR04_004": 20,
            "HCSR04_005": 20,
            "HCSR04_006": 20,
            "HCSR04_007": 20
          },
          {
            "Time": 0,
            "HCSR04_001": 10,
            "HCSR04_002": 60,
            "HCSR04_003": 60,
            "HCSR04_004": 40,
            "HCSR04_005": 50,
            "HCSR04_006": 30,
            "HCSR04_007": 60
          }
      ]
    }

def makeRequest(scoring_uri,key):
  # Convert to JSON string
  input_data = json.dumps(data)
  with open("data.json", "w") as _f:
      _f.write(input_data)

  # Set the content type
  headers = {'Content-Type': 'application/json'}
  # If authentication is enabled, set the authorization header
  headers['Authorization'] = f'Bearer {key}'

  # Make the request and display the response
  resp = requests.post(scoring_uri, input_data, headers=headers)
  print(resp.json())

def main(argv,key,scoring_uri):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:k:u",["ifile=","ofile=","key","uri"])
   except getopt.GetoptError:
      print ('test.py -k <key> -u <uri> -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -k <key> -u <uri> -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in ("-k","--key"):
        key= arg
      elif opt in ("-u","--uri"):
        scoring_uri= arg

   print ('Input file is "', inputfile)
   print ('Output file is "', outputfile)
   print ('Key token is "', key)
   print ('URI token is "', scoring_uri)
   makeRequest(scoring_uri,key)

if __name__ == "__main__":
   main(sys.argv[1:],key,scoring_uri)



