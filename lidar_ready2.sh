#!/bin/bash

# GPIO pin number
gpio_pin=22

# Name of the tmux session
tmux_session="mysession"

# Log file
log_file="/path/to/your/log/file.log"

# Function to check if the tmux session is active
function is_tmux_session_active() {
  tmux has-session -t "$tmux_session" > /dev/null 2>&1
}

# Export the GPIO pin (if necessary, adjust based on your system)
sudo gpio -g mode $gpio_pin out

# Loop indefinitely
while true; do
  if is_tmux_session_active; then
    echo "$(date): Tmux session '$tmux_session' is active." >> "$log_file"
    sudo gpio -g write $gpio_pin 1  # Set GPIO pin high
  else
    echo "$(date): Tmux session '$tmux_session' is not active." >> "$log_file"
    sudo gpio -g write $gpio_pin 0  # Set GPIO pin low
  fi

  sleep 5  # Check every 5 seconds
done
