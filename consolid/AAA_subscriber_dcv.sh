#!/bin/bash

cd ~/cyglidar_ws

source install/setup.bash
source /opt/ros/foxy/setup.bash

cd ~/cyglidar_ws/src/cyglidar_d1/D1_ROS2

sudo python3 gpio_handler3.py


