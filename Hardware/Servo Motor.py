import RPi.GPIO as rp
import time
rp.setwarnings(False)
rp.setmode(rp.BCM)
rp.setup(19,rp.OUT)
p=rp.PWM(19,50)
p.start(12.5)
while 1:
    p.ChangeDutyCycle(7.5)
    time.sleep(1)
    
    p.ChangeDutyCycle(0)
    time.sleep(1)
    
