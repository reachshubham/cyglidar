import RPi.GPIO as GPIO
import time
import csv
import datetime
import pytz # Import pytz for time zone handling

GPIO.setmode(GPIO.BCM)

LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

def update_led(mean_range):
    global last_high_time

    if mean_range is not None and mean_range <= 0.80:
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
        last_save_time = None  # Initialize as None for clarity

        now = datetime.datetime.now(pytz.timezone("EST"))  # Get current time in EST
        filename = f"mean_range_values_{now:%Y-%m-%d_%H-%M-%S}.csv"

        with open(filename, "w", newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Time", "Mean Range"])

            while True:
                try:
                    with open("mean_range.txt", "r") as file:
                        data = file.read().strip()
                        if data:
                            try:
                                mean_range = float(data)
                                update_led(mean_range)

                                # Get current time in EST with milliseconds
                                now = datetime.datetime.now(pytz.timezone("EST"))
                                current_time_est = now.strftime("%Y-%m-%d %H:%M:%S.%f")

                                # Check interval before saving data
                                if last_save_time is None or now - last_save_time >= datetime.timedelta(seconds=1):
                                    last_save_time = now
                                    csv_writer.writerow([current_time_est, mean_range])
                            except ValueError:
                                print("Error converting data to float")
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
