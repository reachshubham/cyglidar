import serial

GPS_PORT = '/dev/ttyACM0'  # Replace with your GPS device's serial port
GPS_BAUDRATE = 9600  # Replace with the correct baud rate for your GPS module

def getGPSData():
    with serial.Serial(GPS_PORT, GPS_BAUDRATE) as ser:
        print(f"Serial port {GPS_PORT} opened successfully.")
        while True:
            try:
                data = ser.readline().decode('utf-8').strip()
                if data.startswith('$GPGGA'):
                    Date, Time, Latitude, Longitude, FixQuality = data.split(',')[1:6]
                    print('Received GPS Data:')
                    print('Date:', Date)
                    print('Time:', Time)
                    print('Latitude:', Latitude)
                    print('Longitude:', Longitude)
                    print('---------------------')
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        getGPSData()
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")
