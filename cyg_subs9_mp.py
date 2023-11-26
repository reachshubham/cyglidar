class CyglidarSubscriber:
    def __init__(self):
        self.mean_range = 0.0
        self.led_status = False
        self.previous_led_status = False
        self.threshold = 0.5  # Threshold to turn on the LED

    def scan_callback(self, scan_data):
        # Accessing laser scan values
        ranges = scan_data.ranges
        angle_min = scan_data.angle_min
        angle_max = scan_data.angle_max
        angle_increment = scan_data.angle_increment

        # Calculate the mean range for angles between +3 and -3 degrees
        sum_range = 0
        count = 0
        for i, scan_range in enumerate(ranges):
            angle = angle_min + i * angle_increment
            degrees = math.degrees(angle)

            if -3 <= degrees <= 3:
                sum_range += scan_range
                count += 1

        if count > 0:
            self.mean_range = sum_range / count

        # Check if the mean_range is below the threshold and the previous LED status is off
        if self.mean_range < self.threshold and not self.previous_led_status:
            self.led_status = True  # Turn on the LED

        # If the mean_range is above the threshold, turn off the LED
        elif self.mean_range >= self.threshold:
            self.led_status = False  # Turn off the LED

        # Update the previous LED status
        self.previous_led_status = self.led_status

        # Write the self.mean_range value to the file (for debugging)
        with open("mean_range.txt", "w") as file:
            file.write(str(self.mean_range))

    def update_led_status(self):
        # This method updates the LED status and can be called from outside the class.
        # It's a more organized way to update the LED status.
        return self.led_status


