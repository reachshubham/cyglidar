import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin connected to the LED
led_pin = 17

# Set the LED pin as an output
GPIO.setup(led_pin, GPIO.OUT)

try:
    # Turn on the LED
    GPIO.output(led_pin, GPIO.HIGH)
    print("LED is ON")
    
    # Wait for 5 seconds
    time.sleep(5)
    
    # Turn off the LED
    GPIO.output(led_pin, GPIO.LOW)
    print("LED is OFF")

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO settings
    GPIO.cleanup()

