import RPi.GPIO as GPIO
import time
import csv
import datetime

GPIO.setmode(GPIO.BCM)

LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

def update_led(mean_range):
    global last_high_time

    if mean_range <= 0.80:
        GPIO.output(LED_PIN, GPIO.HIGH)
        print(f"Signal : ON, mean_range: {mean_range}")
        last_high_time = time.time()
    else:
        if time.time() - last_high_time >= 1:
            GPIO.output(LED_PIN, GPIO.LOW)
            print(f"Signal : OFF, mean_range: {mean_range}")

if __name__ == '__main__':
    try:
        last_high_time = 0
        now = datetime.datetime.now()  # Get current timestamp
        filename = f"mean_range_values_{now:%Y-%m-%d_%H-%M-%S}.csv"  # Generate unique filename

        with open(filename, "w", newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Time", "Mean Range"])

            while True:
                try:
                    with open("mean_range.txt", "r") as file:
                        data = file.read().strip()
                        if data:
                            mean_range = float(data)
                            update_led(mean_range)
                            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                            csv_writer.writerow([current_time, mean_range])
                        else:
                            # Handle empty mean_range.txt file
                            pass

                except FileNotFoundError:
                    print("mean_range.txt file not found")

    except KeyboardInterrupt:
        GPIO.cleanup()
    except Exception as e:
        print(f"An error occurred: {e}")
        GPIO.cleanup()

