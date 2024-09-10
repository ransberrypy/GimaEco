import time
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import ST7789 as ST7789  # TFT display library

# TFT display setup (using ST7789 driver)
disp = ST7789.ST7789(
    height=240,  # Resolution for a 240x240 display (adjust for your screen)
    rotation=180,  # Rotate 180 degrees if necessary
    port=0,
    cs=1,  # SPI chip select (CS)
    dc=9,  # Data/command pin
    rst=25,  # Reset pin
    spi_speed_hz=80 * 1000 * 1000,  # Speed
)

# Initialize display
disp.begin()

# Fake sensor data for demonstration
pre_readings = {"Oxygen": [], "Hydrogen": [], "Nitrogen": []}
post_readings = {"Oxygen": [], "Hydrogen": [], "Nitrogen": []}


# Function to update the sensor readings with random data (replace with actual sensor readings)
def update_sensor_data():
    pre_readings["Oxygen"].append(np.random.uniform(18, 21))  # Example O2 data
    post_readings["Oxygen"].append(np.random.uniform(18, 21))
    pre_readings["Hydrogen"].append(np.random.uniform(0, 5))  # Example H2 data
    post_readings["Hydrogen"].append(np.random.uniform(0, 5))
    pre_readings["Nitrogen"].append(np.random.uniform(70, 80))  # Example N2 data
    post_readings["Nitrogen"].append(np.random.uniform(70, 80))


# Function to plot the graph and display it on the screen
def plot_and_display():
    # Update sensor data
    update_sensor_data()

    # Limit the history to the last 10 values
    for gas in pre_readings.keys():
        if len(pre_readings[gas]) > 10:
            pre_readings[gas].pop(0)
            post_readings[gas].pop(0)

    # Create a matplotlib plot
    plt.figure(figsize=(4, 4))
    gases = ["Oxygen", "Hydrogen", "Nitrogen"]

    for gas in gases:
        plt.plot(pre_readings[gas], label=f"Pre {gas}", linestyle="--", marker="o")
        plt.plot(post_readings[gas], label=f"Post {gas}", linestyle="-", marker="x")

    plt.title("Gas Levels (Pre vs Post)")
    plt.xlabel("Time")
    plt.ylabel("Concentration")
    plt.legend(loc="upper left")
    plt.grid(True)

    # Save the plot as an image
    plt.savefig("/tmp/plot.png", bbox_inches="tight")
    plt.close()

    # Load the saved image and display it on the TFT screen
    image = Image.open("/tmp/plot.png")
    image = image.resize((240, 240))  # Resize the image to fit your screen

    # Display the image on the TFT screen
    disp.display(image)


try:
    while True:
        plot_and_display()  # Update and show the graph
        time.sleep(60)  # Update every 60 seconds

except KeyboardInterrupt:
    disp.cleanup()  # Clean up on Ctrl+C
