import rclpy
from sensor_msgs.msg import LaserScan
import math
import RPi.GPIO as GPIO  # Import the GPIO library

# Define the GPIO pin for the LED
LED_PIN = 17

class CyglidarSubscriber:
    def __init__(self):
        # Initialize the GPIO library
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT)  # Set the LED pin as an output
        self.mean_range = 0.0

    def scan_callback(self, scan_data):
        # Accessing laser scan values
        ranges = scan_data.ranges
        angle_min = scan_data.angle_min
        angle_max = scan_data.angle_max
        angle_increment = scan_data.angle_increment

        # Calculate the mean range for angles between +3 and -3 degrees
        sum_range = 0
        count = 0
        for i, scan_range in enumerate(ranges):
            angle = angle_min + i * angle_increment
            degrees = math.degrees(angle)

            if -3 <= degrees <= 3:
                sum_range += scan_range
                count += 1

        if count > 0:
            self.mean_range = sum_range / count

        # Control the LED based on the mean range
        if self.mean_range > 0.5:
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on the LED
        else:
            GPIO.output(LED_PIN, GPIO.LOW)   # Turn off the LED


def cyglidar_subscriber():
    rclpy.init()

    node = rclpy.create_node('cyglidar_subscriber')

    # Create a CyglidarSubscriber object
    subscriber = CyglidarSubscriber()

    # Subscribe to the /scan topic
    node.create_subscription(LaserScan, '/scan', subscriber.scan_callback, 10)

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    cyglidar_subscriber()

