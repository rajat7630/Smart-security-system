import RPi.GPIO as ir
import json
import time
import requests
ir.setwarnings(False)
ir.setmode(ir.BCM)
ir.setup(21,ir.IN)
while(1):
    a=ir.input(21)
    print(a)
    time.sleep(1)
