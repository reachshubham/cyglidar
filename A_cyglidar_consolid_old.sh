
#!/bin/bash

# Start a new tmux session
tmux new-session -d -s mysession
 
# Split the terminal into three panes and run your scripts
tmux send-keys -t mysession:0.0 '~/cyglidar_ws/src/cyglidar_d1/D1_ROS2/consolid_old/A_cyglidar_launch.sh' C-m
tmux split-window -h -t mysession:0
tmux send-keys -t mysession:0.1 '~/cyglidar_ws/src/cyglidar_d1/D1_ROS2/consolid_old/AA_cyglidar_subscriber.sh' C-m
tmux split-window -h -t mysession:0.1
tmux send-keys -t mysession:0.2 '~/cyglidar_ws/src/cyglidar_d1/D1_ROS2/consolid_old/AAA_subscriber_dcv.sh' C-m

# Attach to the tmux session to see the scripts running
tmux attach-session -t mysession
