#!/usr/bin/python

import xmlrpclib
import time

proxy = xmlrpclib.ServerProxy("http://10.5.5.104:9900/")


proxy.relay_on(0)
time.sleep(1)
proxy.relay_off(0)
time.sleep(1)
proxy.relay_on(1)
time.sleep(1)
proxy.relay_off(1)
time.sleep(1)
proxy.relay_on(2)
time.sleep(1)
proxy.relay_off(2)
time.sleep(1)
proxy.relay_on(3)
time.sleep(1)
proxy.relay_off(3)

time.sleep(1)
proxy.relay_on(4)
time.sleep(1)
proxy.relay_off(4)
time.sleep(1)
proxy.relay_on(5)
time.sleep(1)
proxy.relay_off(5)
time.sleep(1)
proxy.relay_on(6)
time.sleep(1)
proxy.relay_off(6)
time.sleep(1)
proxy.relay_on(7)
time.sleep(1)
proxy.relay_off(7)
