import RPi.GPIO as GPIO
from time import sleep
import subprocess

# Set up GPIO pin 27 using BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)  # Set up the pin
led = GPIO.PWM(27, 50)  # Create PWM object for LED control
led.start(0)  # Start PWM output at 0 duty cycle (LED off)

# Paths to your shell scripts
script1_path = "~/A_cyglidar_consolid_old.sh"

while True:
  try:
    # Check if all scripts are running without errors
    scripts_running = all(subprocess.call(["pgrep", script_name]) == 0
                          for script_name in ["A_cyglidar_consolid.sh"])

    if scripts_running:
      led.ChangeDutyCycle(100)  # Turn LED on at full brightness
      print("All scripts running smoothly, LED on")
    else:
      led.ChangeDutyCycle(0)  # Turn LED off
      print("At least one script not running, LED off")

    sleep(5)  # Check every 5 seconds

  except Exception as e:
    print("Error encountered:", str(e))

GPIO.cleanup()  # Clean up GPIO resources at the end
