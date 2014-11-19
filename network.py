#!/usr/bin/python

import xmlrpclib
import Adafruit_BBIO.GPIO as GPIO
from SimpleXMLRPCServer import SimpleXMLRPCServer

interface = '10.5.5.104'
port = 9900
PIN0 = 'P9_11'
PIN1 = 'P9_12'
PIN2 = 'P9_14'
PIN3 = 'P9_16'


def relay_on(relay_num):
    pin = get_pin(relay_num)
    GPIO.output(pin, GPIO.LOW)
    return True

def relay_off(relay_num):
    pin = get_pin(relay_num)
    GPIO.output(pin, GPIO.HIGH)
    return True

def get_pin(relay_num):
    pins = [PIN0, PIN1, PIN2, PIN3,]
    pin_num = relay_num % 4
    print 'Getting relay', relay_num, '>', pin_num
    return pins[pin_num]
    
GPIO.setup(get_pin(0), GPIO.OUT)
GPIO.setup(get_pin(1), GPIO.OUT)
GPIO.setup(get_pin(2), GPIO.OUT)
GPIO.setup(get_pin(3), GPIO.OUT)



server = SimpleXMLRPCServer((interface, port))
print "Listening on port", port
server.register_function(relay_on, "relay_on")
server.register_function(relay_off, "relay_off")
server.serve_forever()
