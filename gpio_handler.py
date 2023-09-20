import RPi.GPIO as GPIO

# Define the GPIO pin for the LED
LED_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)  # Set the LED pin as an output

def update_led(mean_range):
    # Control the LED based on the mean_range
    if mean_range < 0.5:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on the LED
    else:
        GPIO.output(LED_PIN, GPIO.LOW)   # Turn off the LED

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

