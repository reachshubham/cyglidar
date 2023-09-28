o#!/bin/bash

locale # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US,UTF-8
sudo update-locale LC_ALL=en_US, UTF-8 LANG=en_US, UTF-8
export LANG=en_US, UTF-8

locale # verify settings

sudo apt install software-properties-common
sudo add-apt-repository universe

sudo apt update && sudo apt install curl -y
sudo curl -sSl https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

sudo apt upgrade

sudo apt install ros-foxy-desktop python3-argcomplete

sudo apt install ros-foxy-ros-base python3-argcomplete

sudo apt install ros-dev-tools

source /opt/ros/foxy/setup.bash

mkdir -p ~/cyglidar_ws/src/
cd ~/cyglidar_ws/src/
git clone -b ROS2-v0.3.0 https://github.com/CygLiDAR-ROS/cyglidar_d1.git
cd ..
colcon build
source install/setup.bash

sudo apt install ros-foxy-pcl-conversions

cd ~/cyglidar_ws/src/cyglidar_d1/scripts
chmod +x create_udev_rules.sh
./create_udev_rules.sh

sudo chmod 777 /dev/ttyUSB0

cd ~/cyglidar_ws/src/cyglidar_d1/D1_ROS2
git clone https://github.com/reachshubham/cyglidar.git


