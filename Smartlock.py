import RPi.GPIO as rp
import time
import urllib3
import random
http=urllib3.PoolManager()
import json
rp.setmode(rp.BCM)
rp.setwarnings(False)
rp.setmode(rp.BCM)
rp.setup(19,rp.OUT) #servo
p=rp.PWM(19,50)

p.start(12.5)
rp.setup(21,rp.IN)
# Setup Keypad
MATRIX  = [
        ["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]
]

MATCH_OTP=""
##MASTER_PASS="12345678"
ROW = [4, 14, 15, 17] # BCM numbering
COL = [18, 27, 22, 23] # BCM numbering
for j in range(4):
    rp.setup(COL[j], rp.OUT)
    rp.output(COL[j], 1)
for i in range(4):
    rp.setup(ROW[i], rp.IN, pull_up_down = rp.PUD_UP)
##def password():
##    x=random.randint(1000,9999)
    ##myMessage = twilioClient.messages.create(body = x, from_=myTwilioNumber, to=destCellPhone)
##    return(x)
def random_otp():
    otp = random.randint(100000,999999)
###    sendsms(otp)
    q=http.request('GET',"http://krishnaagarwalkrishnaagarwal.000webhostapp.com/rajat/update.php?id=3&passw="+otp)
    w=q.data.decode("utf-8")
    global MATCH_OTP
    otp = str(otp)
    print (otp)
    MATCH_OTP=otp
    return check_otp(6)
##
##def master_pass():
##    return check_otp(8)

def check_otp(range_digit):
    flag = 0
    option = 0
    ctr = 0
    global MATCH_OTP
    st=""
    if range_digit == 6:
        print("ENTER 6 DIGIT OTP")
        option = 0
    else:
        print("ENTER MASTER PASSWORD")
        option = 1
    while (ctr<3):
        for c in range(range_digit):
            flag = 0
            while(True):
                if flag==1:
                    break
                for j in range(4):
                    rp.output(COL[j],0)
                    for i in range(4):
                        if rp.input(ROW[i]) == 0:                   
                            print (MATRIX[i][j],end = "",flush=True)
                            time.sleep(0.2)
                            while(rp.input(ROW[i]) == 0):
                                pass
                            if MATRIX[i][j]=='A':
                                return 0
                            st = st+str(MATRIX[i][j])
                            flag=1
                    rp.output(COL[j],1)
            if c==5 and option==0:
                if st==MATCH_OTP:
                        print('\n\nOTP MATCHED,DOOR OPENED')
                        p.ChangeDutyCycle(7.5)
                        time.sleep(1)
    
                        p.ChangeDutyCycle(0)
                        time.sleep(1)
                        while(True):
                            a=rp.input(21)
                            if(a==0):
                                p.ChangeDutyCycle(7.5)
                                time.sleep(1)
    
                                p.ChangeDutyCycle(0)
                                time.sleep(1)
                            
                        MATCH_OTP=""
                        return 1
                else:
                    print("\n\nINCORRECT OTP,RETRY AGAIN OR PRESS 'A' TO EXIT")
                    st=""
                    ctr=ctr+1
##            if c==7 and option==1:
##                if st==MASTER_PASS:
##                    print('\n\nPASSWORD MATCHED,DOOR OPENED')
##                    return 1
##                else:
##                    print("\n\nINCORRECT PASSWORD,RETRY AGAIN OR PRESS 'A' TO EXIT")
##                    st=""
##                    ctr=ctr+1
    return 0
def loopover(flag):
    
        if flag==1:
            print("\nPRESS 'A' TO SEND OTP")
        else:
            print("\nPRESS 'D' TO CLOSE DOOR")
        while(True):
            for j in range(4):
                rp.output(COL[j],0)
                for i in range(4):
                    if rp.input(ROW[i]) == 0:                   
                        print (MATRIX[i][j])  
                        time.sleep(0.2)
                        while(rp.input(ROW[i]) == 0):
                            pass
                        if MATRIX[i][j]=='A' and flag==1:
                            state = random_otp()
                rp.output(COL[j],1)
loopover(1)
