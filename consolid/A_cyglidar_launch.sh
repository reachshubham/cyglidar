#!/bin/bash

cd ~/cyglidar_ws

source install/setup.bash
source /opt/ros/foxy/setup.bash

ros2 launch cyglidar_d1_ros2 cyglidar.launch.py

