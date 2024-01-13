from xbee import ZigBee
import serial
ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
zb = ZigBee(ser)
while True:
    data = zb.wait_read_frame()
    print(data)
