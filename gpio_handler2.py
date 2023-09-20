import RPi.GPIO as GPIO
import time

# Define the GPIO pin for the LED
LED_PIN = 17

# Blinking pattern parameters
blink_duration = 1.0  # Duration of each blink cycle (in seconds)
blink_interval = 0.5  # Interval between on and off states (in seconds)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)  # Set the LED pin as an output

def blink_led():
    GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on the LED
    time.sleep(blink_interval)
    GPIO.output(LED_PIN, GPIO.LOW)  # Turn off the LED
    time.sleep(blink_interval)

def update_led(mean_range):
    if mean_range < 0.5:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on the LED
    else:
        # Blink the LED when mean scan range is greater than 0.5 meters
        while mean_range > 0.5:
            blink_led()
            mean_range = 0.0  # Reset mean_range to 0.0 after blinking

if __name__ == '__main__':
    while True:
        # Read the mean_range value from a file, a queue, or any other IPC mechanism.
        # For simplicity, you can use a file for this example.
        try:
            with open("mean_range.txt", "r") as file:
                data = file.read().strip()
                if data:
                    mean_range = float(data)
                else:
                    # Handle the case when the file is empty
                    mean_range = 0.0
        except FileNotFoundError:
            # Handle the case when the file does not exist
            mean_range = 0.0
        except ValueError:
            # Handle the case when the file contains invalid data
            print("Error: Invalid data in the file.")
            mean_range = 0.0

        update_led(mean_range)

