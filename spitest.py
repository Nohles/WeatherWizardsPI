from gpiozero import MCP3008

rain = MCP3008(1)
moist = MCP3008(0)
light = MCP3008(2)
print(moist.value)
print(rain.value)
print(light.value)
