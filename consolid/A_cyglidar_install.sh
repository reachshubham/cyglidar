#!/bin/bash

mkdir -p ~/cyglidar_ws/src/
cd ~/cyglidar_ws/src/
git clone -b ROS2-v0.3.0 https://github.com/CygLiDAR-ROS/cyglidar_d1.git
cd ..
colcon build
source install/setup.bash

sudo apt install ros-{ROS2 Ver Name}-pcl-conversions

cd ~/cyglidar_ws/src/cyglidar_d1/scripts
chmod +x create_udev_rules.sh
./create_udev_rules.sh

sudo chmod 777 /dev/ttyUSB0

cd ~/cyglidar_ws/src/cyglidar_d1/D1_ROS2
git clone https://github.com/reachshubham/cyglidar.git

