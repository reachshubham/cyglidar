import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin connected to the buzzer
buzzer_pin = 17

# Set the buzzer pin as an output
GPIO.setup(buzzer_pin, GPIO.OUT)

try:
    # Turn on the buzzer
    GPIO.output(buzzer_pin, GPIO.HIGH)
    print("Buzzer is ON")
    
    # Wait for 5 seconds
    time.sleep(5)
    
    # Turn off the buzzer
    GPIO.output(buzzer_pin, GPIO.LOW)
    print("Buzzer is OFF")

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
