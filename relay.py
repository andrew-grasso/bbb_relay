#!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
import time

pin = "P9_12"

print "setting up ", pin
GPIO.setup(pin, GPIO.OUT)


GPIO.output(pin, GPIO.LOW)

time.sleep(5)

GPIO.output(pin, GPIO.HIGH)


GPIO.cleanup()


