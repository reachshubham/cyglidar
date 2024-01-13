import subprocess
from xbee import ZigBee
import serial

def start_minicom(serial_port):
    minicom_command = f"sudo minicom -b 9600 -o -D {serial_port}"
    subprocess.run(minicom_command, shell=True)

try:
    # Open serial port
    ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
    print("Serial port opened successfully")

    # Create ZigBee object
    zb = ZigBee(ser)
    print("ZigBee object created successfully")

    # Start minicom to monitor data
    start_minicom('/dev/ttyS0')

    while True:
        try:
            # Wait for and read a frame
            frame = zb.wait_read_frame()
            print("Received frame:", frame)

            # Access data within the frame
            data = frame["rf_data"].decode("utf-8")
            print("Decoded data:", data)

        except Exception as e:
            print("Error reading frame:", str(e))

except Exception as e:
    print("Error opening serial port:", str(e))

finally:
    # Close the serial port to release resources
    if ser.is_open:
        ser.close()
        print("Serial port closed")
