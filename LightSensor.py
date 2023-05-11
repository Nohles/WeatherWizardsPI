from gpiozero import LightSensor
from time import sleep

ldr = LightSensor(24)
#ldr.wait_for_dark()
while True:
	print(ldr.value)
	#print("light detected")
	sleep(2)
