l#!/bin/bash

cd ~/cyglidar_ws

source install/setup.bash
source /opt/ros/foxy/setup.bash

cd ~/cyglidar_ws/src/cyglidar_d1/D1_ROS2/cyglidar/consolid
sudo apt install gpiod
sudo apt install wiringpi
sudo su
ls -l/sys/class/gpio
chmod 666/sys/class/gpio/*

sudo python3 gpio_handler3.py


