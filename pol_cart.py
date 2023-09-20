#!/usr/bin/env python

import rclpy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Point
from std_msgs.msg import Float32MultiArray  # Import Float32MultiArray for Cartesian data

from math import cos, sin

def scan_callback(scan_data, cartesian_publisher):
    # Accessing laser scan values
    ranges = scan_data.ranges
    angle_min = scan_data.angle_min
    angle_increment = scan_data.angle_increment

    cartesian_data = Float32MultiArray()  # Create a Float32MultiArray

    # Calculate and store Cartesian coordinates
    for i, scan_range in enumerate(ranges):
        angle = angle_min + i * angle_increment
        x = scan_range * cos(angle)  # Convert to Cartesian x
        y = scan_range * sin(angle)  # Convert to Cartesian y
        cartesian_data.data.extend([x, y])  # Append x and y to data array

        # Print Cartesian coordinates for debugging
        print(f"Point {i}: X: {x:.2f}, Y: {y:.2f}")

    # Publish the Cartesian coordinates
    cartesian_publisher.publish(cartesian_data)


def cyglidar_subscriber():
    rclpy.init()
    node = rclpy.create_node('cyglidar_subscriber')

    # Create a publisher for Cartesian data
    cartesian_publisher = node.create_publisher(Float32MultiArray, '/cartesian_scan', 10)

    # Subscribe to the /scan topic
    scan_subscription = node.create_subscription(LaserScan, '/scan',
                                                  lambda msg: scan_callback(msg, cartesian_publisher), 10)

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    cyglidar_subscriber()

