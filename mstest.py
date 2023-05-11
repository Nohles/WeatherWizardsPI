from bluedot.btcomm import BluetoothServer
from signal import pause
import requests
from gpiozero import LightSensor
from time import sleep
from gpiozero import DigitalInputDevice
import re,uuid
import dht11
import json
import time
from gpiozero import MCP3008


def getLiveSensorData():
    ldr = MCP3008(4)
    norain = MCP3008(1)
    nomoisture = MCP3008(0)
    ph = MCP3008(3)
    instance = dht11.DHT11(pin=19)
    result = instance.read()
    temperature = result.temperature
    humidity = result.humidity
    while humidity == 0 and temperature == 0:
        sleep(1)
        #humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        result = instance.read()
        temperature = result.temperature
        humidity = result.humidity
    temp = ((temperature * 1.8) +32)
    # print("Temp={0:0.1f}F  Humidity={1:0.1f}%".format(temp, humidity))
    # print(ldr.raw_value)
    # print(nomoisture.raw_value)
    phnum = (((-5.94)* ph.voltage) + 22)
    s.send("1,"+str(temp)+","+ str(humidity) +","+ str(ldr.raw_value) +","+ str(norain.value) +","+ str(nomoisture.raw_value) +","+ str(phnum)+"\n")

def AdvRun(userChoice):
    runName = userChoice[1]
    strduration = userChoice[2]
    duration = float(strduration)
    runID = userChoice[3]
    start_time = time.time()
    macAddress=''.join(re.findall('..', '%012x' % uuid.getnode()))
    

    ldr = MCP3008(4)
    norain = MCP3008(1)
    nomoisture = MCP3008(0)
    ph = MCP3008(3)

    timeToEnd = duration

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > duration:
            print("complete")
            break
        instance = dht11.DHT11(pin=13)
        result = instance.read()
        temperature = result.temperature
        humidity = result.humidity
        
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
        s.send("2,"+str(temp)+","+ str(humidity) +","+ str(ldr.raw_value) +","+ str(norain.value) +","+ str(nomoisture.raw_value) +","+ str(phnum)+"\n")
        sleep(20)












def data_received(data):
    print(data)
    userChoice = data.split(",")
    print(userChoice[0])
    if data[0] == "1":
        getLiveSensorData()
    if data[0] == "2":
        AdvRun(userChoice)
    

    
    




s = BluetoothServer(data_received)
pause()
