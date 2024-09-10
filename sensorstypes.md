1. Oxygen Sensor:
Sensor Type: Electrochemical sensors are often used to measure oxygen levels in the air because they are precise and widely available.
Example Sensors:
MQ-135: This sensor can detect various gases, including oxygen, but it is primarily used for air quality measurements (CO₂, NH₃, alcohol, benzene, etc.).
<strong>ZE07-O2</strong>: A dedicated oxygen sensor that can directly measure the oxygen concentration in the air, commonly used in Raspberry Pi or Arduino projects.
SEN0322 (Gravity: I2C Oxygen Sensor): A high-quality sensor that works with microcontrollers to provide accurate oxygen concentration readings.

2. Nitrogen Sensor:
Measuring Nitrogen: Measuring nitrogen directly in the air can be tricky because it comprises about 78% of the atmosphere, and its concentration is relatively stable. However, if you want to monitor nitrogen oxide (NOx) gases (like NO or NO₂, often relevant in pollution measurements), there are sensors for that.
Example Sensors:
MQ-136: This sensor can detect nitrogen compounds like hydrogen sulfide (H₂S), but can be adapted for some nitrogen gas monitoring applications.
<b>MICS-2714</b>: A sensor designed to detect NO₂ levels.
MiCS-5524: Another option for detecting NO₂, commonly used for air quality monitoring.

3. Air Quality Sensors (Combination Sensors):
BME680: This is a popular sensor for air quality, which can detect volatile organic compounds (VOC), temperature, humidity, and gas concentrations in the air. It doesn’t measure pure nitrogen or oxygen levels but can give you an overview of air quality.

MQ-135: This multi-gas sensor can measure a variety of gases including CO₂, NH₃, benzene, alcohol, and sometimes volatile organic compounds (VOC). While it does not directly measure nitrogen or oxygen, it can give a general indication of air quality.