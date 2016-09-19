#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Declare State  :  True if pin 4 on GND
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Declare interrupt
GPIO.add_event_detect(4, GPIO.BOTH)

while True:
    if GPIO.event_detected(4):
        now = time.strftime("%c")
        if GPIO.input(4) == False:
            print ("ON	" + now)
            f = open ("logPAC.log", "a")
            f.write ("ON	" + now+ '\n')
            f.close ()
        else:
            print ("OFF	" + now)
            f = open ("logPAC.log", "a")
            f.write ("OFF	" + now+ '\n')
            f.close ()
        # anti-bounce
        time.sleep(1)