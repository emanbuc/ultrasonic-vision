import os 
import time  
from time import sleep,strftime
from datetime import datetime 

filename= strftime("%Y%m%d_%H%M%S")+".csv"

file = open(filename, "w+") 
i=0 
if os.stat(filename).st_size == 0: 
        file.write("Time,Sensor1,Sensor2,Sensor3,Sensor4,Sensor5\n") 
while i<10: 
        i=i+1 
        now = datetime.now() 
        file.write(str(now)+","+str(i)+","+str(-i)+","+str(i-10)+","+str(i+5)+","+str(i*i)+"\n") 
        file.flush() 
        time.sleep(5)
        
file.close() 