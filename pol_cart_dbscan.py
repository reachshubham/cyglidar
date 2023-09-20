import csv
import numpy as np
from math import sin, cos
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32MultiArray
from sklearn.cluster import DBSCAN

X_THRESHOLD = 10.0  # Adjust as needed
Y_THRESHOLD = 10.0  # Adjust as needed
EPSILON = 0.5  # DBSCAN epsilon parameter
MIN_SAMPLES = 5  # DBSCAN min_samples parameter

CSV_FILE_PATH = "/home/koc1501/cyglidar_ws/src/cyglidar_d1/scanned_coordinates.csv"  # Specify the path for the CSV file

def scan_callback(scan_data, cartesian_publisher):
    print("Received LIDAR data")  # Debugging statement

    # Accessing laser scan values
    ranges = scan_data.ranges
    angle_min = scan_data.angle_min
    angle_increment = scan_data.angle_increment

    cartesian_data = Float32MultiArray()  # Create a Float32MultiArray

    # Calculate and store Cartesian coordinates
    scanned_coordinates = []  # List to store all scanned coordinates

    for i, scan_range in enumerate(ranges):
        angle = angle_min + i * angle_increment
        x = scan_range * cos(angle)  # Convert to Cartesian x
        y = scan_range * sin(angle)  # Convert to Cartesian y

        # Check if the point falls within the acceptable range
        if abs(x) <= X_THRESHOLD and abs(y) <= Y_THRESHOLD:
            cartesian_data.data.extend([x, y])  # Append x and y to data array
            scanned_coordinates.append([x, y])  # Append to the list

    print(f"Total points before filtering: {len(cartesian_data.data) // 2}")  # Debugging statement

    # Apply DBSCAN to filter noisy points
    cartesian_points = np.array(cartesian_data.data).reshape(-1, 2)
    dbscan = DBSCAN(eps=EPSILON, min_samples=MIN_SAMPLES)
    dbscan_labels = dbscan.fit_predict(cartesian_points)

    filtered_data = []
    for i, label in enumerate(dbscan_labels):
        if label != -1:  # -1 labels indicate noisy points
            filtered_data.extend(cartesian_points[i])

    print(f"Total points after filtering: {len(filtered_data) // 2}")  # Debugging statement

    # Print the Cartesian coordinates before publishing
    print("Filtered Cartesian Coordinates:")
    for i in range(0, len(filtered_data), 2):
        x = filtered_data[i]
        y = filtered_data[i + 1]
        print(f"X: {x}, Y: {y}")

    # Write scanned coordinates to a CSV file
    with open(CSV_FILE_PATH, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["X", "Y"])  # Write header
        for coord in scanned_coordinates:
            csvwriter.writerow(coord)

    # Publish the filtered Cartesian coordinates
    filtered_cartesian_data = Float32MultiArray(data=filtered_data)
    cartesian_publisher.publish(filtered_cartesian_data)

# Debugging statements
print("Starting the script")

# Replace with your ROS2 setup and subscription code

# Debugging statements
print("Subscribed to LIDAR data")

# Replace with code for publishing and spinning ROS2 node

# Debugging statements
print("Node is spinning")

