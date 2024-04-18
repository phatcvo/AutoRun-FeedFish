import RPi.GPIO as GPIO
import time

# GPIO pin connected to the servo
SERVO_PIN = 18

try:
    # Initialize GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SERVO_PIN, GPIO.OUT)

    # Create PWM object
    pwm = GPIO.PWM(SERVO_PIN, 50)  # 50 Hz (20 ms period)

    # Function to set servo angle
    def set_angle(angle):
        duty_cycle = (angle / 18) + 2.5  # Convert angle to duty cycle (2.5 - 12.5)
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.5)  # Wait for servo to reach the position

    while True:
        # Define the desired time to run the script (e.g., 12:00 PM)
        desired_hour = 12
        desired_minute = 0

        # Calculate the time until the desired time
        now = time.localtime()
        desired_time = time.struct_time((now.tm_year, now.tm_mon, now.tm_mday, desired_hour, desired_minute, 0, now.tm_wday, now.tm_yday, now.tm_isdst))
        time_until_run = time.mktime(desired_time) - time.mktime(now)
        if time_until_run < 0:
            time_until_run += 86400  # Add 24 hours if the desired time has already passed

        # Sleep until the desired time
        print("Waiting for", round(time_until_run / 3600, 2), "hours until the next run.")
        time.sleep(time_until_run)

        # Start PWM
        pwm.start(0)

        # Run the script
        print("Script is now running.")

        # Rotate servo to different angles
        for i in range(15):
            set_angle(0)
            time.sleep(0.2)
            set_angle(180)
            time.sleep(0.2)


finally:
    # Clean up GPIO
    pwm.stop()
    GPIO.cleanup()
