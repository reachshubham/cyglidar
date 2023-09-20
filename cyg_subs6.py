import rclpy
from sensor_msgs.msg import LaserScan
import math


class CyglidarSubscriber:
    def scan_callback(self, scan_data):
        # Accessing laser scan values
        ranges = scan_data.ranges
        angle_min = scan_data.angle_min
        angle_max = scan_data.angle_max
        angle_increment = scan_data.angle_increment

        # Print the range values for angles between +3 and -3 degrees
        for i, scan_range in enumerate(ranges):
            angle = angle_min + i * angle_increment
            degrees = math.degrees(angle)

            if -3 <= degrees <= 3:
                print(f"Angle: {degrees:.2f} degrees, Range: {scan_range:.2f} meters")


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

