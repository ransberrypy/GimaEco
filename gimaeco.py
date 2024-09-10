import time
import csv
import RPi.GPIO as GPIO

# GPIO pin definitions for the sensors
OXYGEN_PRE_PIN = 17
OXYGEN_POST_PIN = 27
HYDROGEN_PRE_PIN = 22
HYDROGEN_POST_PIN = 5
NITROGEN_PRE_PIN = 6
NITROGEN_POST_PIN = 13

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(OXYGEN_PRE_PIN, GPIO.IN)
GPIO.setup(OXYGEN_POST_PIN, GPIO.IN)
GPIO.setup(HYDROGEN_PRE_PIN, GPIO.IN)
GPIO.setup(HYDROGEN_POST_PIN, GPIO.IN)
GPIO.setup(NITROGEN_PRE_PIN, GPIO.IN)
GPIO.setup(NITROGEN_POST_PIN, GPIO.IN)

def read_sensor(sensor_pin):
    # Simulate reading sensor data. Replace this with actual sensor reading code.
    return GPIO.input(sensor_pin)

def save_readings(oxygen_pre, oxygen_post, hydrogen_pre, hydrogen_post, nitrogen_pre, nitrogen_post, timestamp):
    with open('gas_readings.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, oxygen_pre, oxygen_post, hydrogen_pre, hydrogen_post, nitrogen_pre, nitrogen_post])

def calculate_difference(pre_value, post_value):
    return post_value - pre_value

def monitor_gas_levels():
    try:
        while True:
            # Get the current timestamp
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            
            # Read sensor values for oxygen, hydrogen, and nitrogen pre and post
            oxygen_pre = read_sensor(OXYGEN_PRE_PIN)
            oxygen_post = read_sensor(OXYGEN_POST_PIN)
            hydrogen_pre = read_sensor(HYDROGEN_PRE_PIN)
            hydrogen_post = read_sensor(HYDROGEN_POST_PIN)
            nitrogen_pre = read_sensor(NITROGEN_PRE_PIN)
            nitrogen_post = read_sensor(NITROGEN_POST_PIN)
            
            # Save the readings
            save_readings(oxygen_pre, oxygen_post, hydrogen_pre, hydrogen_post, nitrogen_pre, nitrogen_post, timestamp)
            
            # Calculate the differences for each gas
            oxygen_diff = calculate_difference(oxygen_pre, oxygen_post)
            hydrogen_diff = calculate_difference(hydrogen_pre, hydrogen_post)
            nitrogen_diff = calculate_difference(nitrogen_pre, nitrogen_post)
            
            # Display the differences
            print(f"Timestamp: {timestamp}")
            print(f"Oxygen Difference: {oxygen_diff}")
            print(f"Hydrogen Difference: {hydrogen_diff}")
            print(f"Nitrogen Difference: {nitrogen_diff}")
            print("--------------------------------------")
            
            # Wait for a few minutes before reading again
            time.sleep(300)  # 300 seconds = 5 minutes (adjust as needed)

    except KeyboardInterrupt:
        print("Stopping gas level monitoring.")
    finally:
        GPIO.cleanup()

# Run the monitoring function
monitor_gas_levels()
