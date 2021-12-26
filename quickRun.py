import Adafruit_DHT
import requests
from gpiozero import LightSensor
from time import sleep
from gpiozero import DigitalInputDevice
import re,uuid
import json

macAddress=''.join(re.findall('..', '%012x' % uuid.getnode()))
print(macAddress)
macAddress
ldr = LightSensor(17)
norain = DigitalInputDevice(21)
nomoisture = DigitalInputDevice(20)
userID = 1
timeToEnd = 5
name =""
r = requests.post("http://api.nohles.dev/api/runs/create.php?userID="+ str(userID) +"&timeToEnd="+ str(timeToEnd)+"&runName="+ name  +"&macAddress="+str(macAddress))

data = r.json()
runID = data["runID"]
print(runID)

#while True:
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
requests.get("https://api.nohles.dev/api/sensor/create.php?temp="+str(temperature)+"&humidity="+str(humidity)+"&light="+str(ldr.value)+"&rain="+str(norain.value)+"&moisture="+str(nomoisture.value)+"&macAddress="+str(macAddress)+"&runID=$
#       sleep(5)
