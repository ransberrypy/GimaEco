import time
import csv
import RPi.GPIO as GPIO

# Define the GPIO pins for the pre and post sensors
PRE_SENSOR_PIN = 17  # Example GPIO pin for pre-sensor
POST_SENSOR_PIN = 27  # Example GPIO pin for post-sensor

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(PRE_SENSOR_PIN, GPIO.IN)
GPIO.setup(POST_SENSOR_PIN, GPIO.IN)

# Function to read from a sensor
def read_sensor(sensor_pin):
    # Replace this with actual sensor reading logic
    return GPIO.input(sensor_pin)

# Function to save readings to a CSV file
def save_readings(pre_value, post_value, timestamp):
    with open('sensor_readings.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, pre_value, post_value])

# Function to calculate the difference
def calculate_difference(pre_value, post_value):
    return post_value - pre_value

try:
    while True:
        # Get the current time
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        # Read sensor values
        pre_value = read_sensor(PRE_SENSOR_PIN)
        post_value = read_sensor(POST_SENSOR_PIN)

        # Save the readings to a file
        save_readings(pre_value, post_value, timestamp)

        # Calculate and display the difference
        difference = calculate_difference(pre_value, post_value)
        print(f"Timestamp: {timestamp} | Pre: {pre_value} | Post: {post_value} | Difference: {difference}")

        # Wait before taking the next reading
        time.sleep(2)  # Adjust the sleep time as needed

except KeyboardInterrupt:
    print("Stopping the sensor reading process.")
finally:
    # Clean up GPIO pins when done
    GPIO.cleanup()
