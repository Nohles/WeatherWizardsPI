from bluedot.btcomm import BluetoothServer
from signal import pause

def data_received(data):
    print(data)
    msg = "testing"
    s.send("testing 1, 2, 3")

s = BluetoothServer(data_received)
pause()
