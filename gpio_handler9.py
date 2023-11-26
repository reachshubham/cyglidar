import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)

LED_PIN_1 = 17
LED_PIN_2 = 18

GPIO.setup(LED_PIN_1, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)

mean_range_buffer = []  # Buffer for storing mean_range values

def update_led(mean_range):
    if mean_range <= 0.5:
        GPIO.output(LED_PIN_1, GPIO.HIGH)
        GPIO.output(LED_PIN_2, GPIO.LOW)
    else:
        GPIO.output(LED_PIN_1, GPIO.LOW)
        GPIO.output(LED_PIN_2, GPIO.HIGH)

def print_values():
    global mean_range_buffer

    while True:
        if mean_range_buffer:
            # Print the accumulated mean_range values
            for mean_range in mean_range_buffer:
                print(f"Signal : mean_range: {mean_range}")

            # Clear the buffer
            mean_range_buffer = []

        time.sleep(1)  # Print every second

def read_mean_range():
    while True:
        try:
            with open("mean_range.txt", "r") as file:
                data = file.read().strip()
                if data:
                    mean_range = float(data)
                    update_led(mean_range)  # Update LED based on mean_range
                    mean_range_buffer.append(mean_range)  # Add mean_range to buffer
                else:
                    print("Error: Empty data in the file.")
        except FileNotFoundError:
            print("Error: File not found.")
        except ValueError:
            print("Error: Invalid data in the file.")

        time.sleep(0.1)  # Check file every 0.1 seconds

if __name__ == '__main__':
    try:
        # Start background threads for printing and file reading
        print_thread = threading.Thread(target=print_values)
        read_thread = threading.Thread(target=read_mean_range)
        print_thread.start()
        read_thread.start()

        # Wait for keyboard interrupt to terminate the program
        while True:
            pass
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
