import serial

def try_baud_rate(baud_rate):
    try:
        with serial.Serial('/dev/ttyACM0', baud_rate, timeout=1) as ser:
            print(f"Trying Baud Rate: {baud_rate}")
            data = ser.readline().decode('utf-8').strip()
            print('Received Data:', data)
            return True
    except serial.SerialException:
        return False

baud_rates_to_try = [9600, 4800, 115200]  # Add more common baud rates if needed

for baud_rate in baud_rates_to_try:
    if try_baud_rate(baud_rate):
        break
