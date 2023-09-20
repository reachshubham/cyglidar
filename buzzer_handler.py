import RPi.GPIO as GPIO
import time

# Define the GPIO pin for the buzzer
BUZZER_PIN = 17

# Sound parameters
buzz_duration = 1.0  # Duration of each buzz cycle (in seconds)
buzz_interval = 0.5  # Interval between on and off states of the buzzer (in seconds)

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)  # Set the buzzer pin as an output

def buzz():
    GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Turn on the buzzer
    time.sleep(buzz_duration)
    GPIO.output(BUZZER_PIN, GPIO.LOW)  # Turn off the buzzer
    time.sleep(buzz_interval)

def update_buzzer(mean_range):
    if mean_range < 0.5:
        GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Turn on the buzzer
    else:
        # Buzz the buzzer when mean scan range is greater than 0.5 meters
        while mean_range > 0.5:
            buzz()
            mean_range = 0.0  # Reset mean_range to 0.0 after buzzing

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

        update_buzzer(mean_range)
