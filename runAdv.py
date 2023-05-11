#import Adafruit_DHT
import requests
from gpiozero import LightSensor
from time import sleep
from gpiozero import DigitalInputDevice
import re,uuid
import dht11
import json
import time
from gpiozero import MCP3008

start_time = time.time()

var = input("Enter how long you would like the pi to run for(in minutes): ")
time_user = int(var) *60

macAddress=''.join(re.findall('..', '%012x' % uuid.getnode())) 
print(macAddress)
macAddress
ldr = MCP3008(4)
norain = MCP3008(1)
nomoisture = MCP3008(0)
ph = MCP3008(3)
userID = 1
timeToEnd = time_user
name =""
r = requests.post("http:// *website* /api/runs/create.php?userID="+ str(userID) +"&timeToEnd="+ str(timeToEnd)+"&runName="+ name  +"&macAddress="+str(macAddress))

data = r.json()
runID = data["runID"]
print(runID)

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time > time_user:
        print("complete")
        break

   # DHT_SENSOR = Adafruit_DHT.DHT11
    #DHT_PIN = 13
    #humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    instance = dht11.DHT11(pin=19)
    result = instance.read()
    temperature = result.temperature
    humidity = result.humidity
    #print("Temp={0:0.1f}F  Humidity={1:0.1f}%".format(temp, humidity))
    
    while humidity == 0 and temperature == 0:
        sleep(1)    
        #humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        result = instance.read()
        temperature = result.temperature
        humidity = result.humidity
    temp = ((temperature * 1.8) +32)
    print("Temp={0:0.1f}F  Humidity={1:0.1f}%".format(temp, humidity))
    print(ldr.raw_value)
    print(norain.value) 
    print(nomoisture.raw_value)
    phnum = (((-5.94)* ph.voltage) + 22)
    print(phnum)
    requests.get("https:// *website* /api/sensor/create.php?temp="+str(temp)+"&humidity="+str(humidity)+"&light="+str(ldr.raw_value)+"&rain="+str(norain.value)+"&moisture="+str(nomoisture.raw_value)+"&PH="+str(phnum)+"&macAddress="+str(macAddress)+"&runID="+str(runID))
    sleep(20)
    
    #  if moisture_value >= 930:
    #print(" No water, Can you plaease water me")
  #elif moisture_value < 930 and moisture_value >= 350:
   # print(" I'm sufficient ")
 # elif moisture_value < 350 :
    #print(" Stop drowning me!")
