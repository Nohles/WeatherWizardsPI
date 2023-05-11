from gpiozero import MCP3008
from time import sleep
ph = MCP3008(3)


#print(phnum)
while True:
    phnum = (((-5.94)* ph.voltage) + 22)
    light = MCP3008(4)
    print(phnum)
    #print(light.raw_value)
    sleep(2)
