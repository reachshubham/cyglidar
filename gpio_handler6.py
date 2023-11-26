from gpiozero import LED, Device
from gpiozero.pins.mock import MockFactory
import time

# Set the pin factory to MockFactory, which doesn't require root access
Device.pin_factory = MockFactory()

LED_PIN = 17
led = LED(LED_PIN)

def update_led(mean_range):
    if mean_range <= 0.5:
        led.on()  # Turn on the LED
        print(f"Signal : ON, mean_range: {mean_range}")
    else:
        led.off()  # Turn off the LED
        print(f"Signal : OFF, mean_range: {mean_range}")

if __name__ == '__main__':
    try:
        while True:
            try:
                with open("mean_range.txt", "r") as file:
                    data = file.read().strip()
                    if data:
                        mean_range = float(data)
                        update_led(mean_range)  # Set the LED status only when data is successfully read and converted
                    else:
                        print("Error: Empty data in the file.")
            except FileNotFoundError:
                print("Error: File not found.")
            except ValueError:
                print("Error: Invalid data in the file.")
            time.sleep(1)  # Add a short delay to avoid excessive console output
    except KeyboardInterrupt:
        pass
    finally:
        pass  # No need for GPIO.cleanup() when using GPIO Zero

