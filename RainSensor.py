from time import sleep
from gpiozero import DigitalInputDevice

norain = DigitalInputDevice(13)

while True:
	print(norain.value)
	#if not norain.is_active:
		#print("it is raining")
	sleep(2)
