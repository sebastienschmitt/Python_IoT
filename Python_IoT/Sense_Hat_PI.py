#!/usr/bin/python
import sys
from sense_hat import SenseHat
import time

# To get good results with the magnetometer you must first calibrate it using
# the program in RTIMULib/Linux/RTIMULibCal
# The calibration program will produce the file RTIMULib.ini
# Copy it into the same folder as your Python code

sense = SenseHat()
while True:
    humidity = sense.get_humidity()
    temp = sense.get_temperature_from_humidity()
    pressure = sense.get_pressure()
    print "Humidite relative :" , humidity, "%"
    print "Temp reel :" , temp, "C"
    print "Pression actuelle : ", pressure
    time.sleep(1000)