from time import sleep
from gpiozero import DigitalInputDevice

norain = DigitalInputDevice(5)
print(norain.value)
#while True:
 #   if not norain.is_active:
  #      print("it has moisture")
   # sleep(2)

