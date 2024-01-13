import serial
import logging
import csv

GPS_PORT = '/dev/ttyACM0'  # Replace with your GPS device's serial port
GPS_BAUDRATE = 9600  # Replace with the correct baud rate for your GPS module

def getGPSData():
    logging.basicConfig(filename='gps_data.log', level=logging.DEBUG)

    with serial.Serial(GPS_PORT, GPS_BAUDRATE) as ser, open('gps_data.csv', 'w', newline='') as csvfile:
        print(f"Serial port {GPS_PORT} opened successfully.")
        logging.info(f"Serial port {GPS_PORT} opened successfully.")
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Date', 'Time', 'Latitude', 'Longitude', 'Fix Quality'])

        while True:
            try:
                data = ser.readline().decode('utf-8').strip()
                logging.debug(f"Received raw data: {data}")

                if data.startswith('$GPGGA'):
                    fields = data.split(',')
                    if len(fields) >= 6:
                        Date, Time, Latitude, Longitude, FixQuality = fields[1:6]
                        print('Received GPS Data:')
                        print('Date:', Date)
                        print('Time:', Time)
                        print('Latitude:', Latitude)
                        print('Longitude:', Longitude)
                        print('Fix Quality:', FixQuality)
                        print('---------------------')
                        logging.info(f"Received GPS data: {Date}, {Time}, {Latitude}, {Longitude}, {FixQuality}")
                        csv_writer.writerow([Date, Time, Latitude, Longitude, FixQuality])
                else:
                    logging.debug(f"Ignoring non-GPGGA sentence: {data}")

            except Exception as e:
                print(f"An error occurred: {e}")
                logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        getGPSData()
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}")
