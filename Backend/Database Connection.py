import serial
import time
import json
import requests
ser =serial.Serial()
ser.port="/dev/ttyACM0"
ser.baudrate= 9600
while(True):
    ser.open()
    readline=ser.readall()
    print (readline)
    result= requests.post('https://smart-lock-a8a7f.firebaseio.com/'+'text.json', data=json.dumps(readline))
    ser.close()
