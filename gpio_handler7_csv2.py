import RPi.GPIO as GPIO
import time
import csv

GPIO.setmode(GPIO.BCM)

LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

def update_led(mean_range):
    if mean_range <= 0.80:
        GPIO.output(LED_PIN, GPIO.HIGH)
        print(f"Signal : ON, mean_range: {mean_range}")
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
        print(f"Signal : OFF, mean_range: {mean_range}")

if __name__ == '__main__':
    try:
        with open("mean_range_values.csv", "w", newline='') as csvfile:
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
                            print("Error: Empty data in the file.")
                except FileNotFoundError:
                    print("Error: File not found.")
                except ValueError:
                    print("Error: Invalid data in the file.")
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

# Function definition is already provided above, so it's removed here
