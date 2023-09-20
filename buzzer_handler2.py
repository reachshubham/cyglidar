import RPi.GPIO as GPIO
import time

# Define the GPIO pin for the buzzer
BUZZER_PIN = 17

# Sound parameters
buzz_frequency = 2000  # Frequency of the buzzer (in Hz)
buzz_duty_cycle = 50   # Duty cycle (0-100) for controlling loudness

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)  # Set the buzzer pin as an output

# Initialize PWM with the specified frequency and duty cycle
buzzer_pwm = GPIO.PWM(BUZZER_PIN, buzz_frequency)
buzzer_pwm.start(buzz_duty_cycle)

def update_buzzer(mean_range):
    if mean_range < 0.5:
        # Stop the buzzer (set duty cycle to 0) when mean_range is less than 0.5 meters
        buzzer_pwm.ChangeDutyCycle(0)
    else:
        # Set the desired duty cycle to control the loudness when mean_range is greater than 0.5 meters
        buzzer_pwm.ChangeDutyCycle(buzz_duty_cycle)

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
