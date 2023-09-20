#!/usr/bin/env python

import rclpy
from sensor_msgs.msg import LaserScan


def scan_callback(scan_data):
    # Accessing laser scan values
    ranges = scan_data.ranges
    angle_min = scan_data.angle_min
    angle_max = scan_data.angle_max
    angle_increment = scan_data.angle_increment

    # Print some information
    print("Number of scan ranges:", len(ranges))
    print("Angle Min:", angle_min)
    print("Angle Max:", angle_max)
    print("Angle Increment:", angle_increment)

    # Print all the scan values
    for i, scan_range in enumerate(ranges):
        angle = angle_min + i * angle_increment
        print(f"Angle: {angle:.2f} radians, Range: {scan_range:.2f} meters")


def cyglidar_subscriber():
    rclpy.init()
    node = rclpy.create_node('cyglidar_subscriber')

    # Subscribe to the /scan topic
    node.create_subscription(LaserScan, '/scan', scan_callback, 10)

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    cyglidar_subscriber()
