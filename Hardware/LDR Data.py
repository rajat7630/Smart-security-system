import RPi.GPIO as rp
import time
import urllib3
import json
rp.setwarnings(False)
rp.setmode(rp.BCM)
rp.setup(8,rp.IN)
http=urllib3.PoolManager()
while(True):
    a=rp.input(8)
    print(a)
    if(a==1):
        print(a)
        q=http.request('GET',"http://krishnaagarwalkrishnaagarwal.000webhostapp.com/rajat/update.php?id=1&status=off")
        w=q.data.decode("utf-8")
        print("off")
    else:
        q=http.request('GET',"http://krishnaagarwalkrishnaagarwal.000webhostapp.com/rajat/update.php?id=1&status=on")
        w=q.data.decode("utf-8")
        print("on")
