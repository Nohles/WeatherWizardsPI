import Adafruit_DHT
import requests
from gpiozero import LightSensor
from time import sleep
from gpiozero import DigitalInputDevice
import re,uuid
import json
import time


start_time = time.time()

var = input("Enter how long you would like the pi to run for(in minutes): ")
time_user = int(var) *60

macAddress=''.join(re.findall('..', '%012x' % uuid.getnode()))
print(macAddress)
macAddress
ldr = LightSensor(17)
norain = DigitalInputDevice(21)
nomoisture = DigitalInputDevice(20)
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

    DHT_SENSOR = Adafruit_DHT.DHT11
    DHT_PIN = 19
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    while humidity is None and temperature is None:
        sleep(1)
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

    print("Temp={0:0.1f}C  Humidity={1:0.1f}%".format(temperature, humidity))
    print(ldr.value)
    print(norain.value)
    print(nomoisture.value)
    requests.get("https:// *website*  /api/sensor/create.php?temp="+str(temperature)+"&humidity="+str(humidity)+"&light="+str(ldr.value)+"&rain="+str(norain.value)+"&moisture="+str(nomoisture.value)+"&macAddress="+str(macAddress)+"&ru$
    sleep(5)

