
#!/bin/bash

cd ~/cyglidar_ws

source install/setup.bash
source /opt/ros/foxy/setup.bash

cd ~/cyglidar_ws/src/cyglidar_d1/D1_ROS2

echo koc150 | sudo -S python3 gpio_handler7.py

