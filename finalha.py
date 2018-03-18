import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

#Distance and Angle obtained
file=open("xyz.txt","r")
contents=file.read()
distance=contents[contents.find(":")+1:contents.find("\n")]
file.seek(contents.find(":")+1)
contents=file.read()
angle=contents[contents.find(":")+1:]

throttle = GPIO.PWM(12, 50) # channel=12 frequency=50Hz
throttle.start(0)
pitch = GPIO.PWM(13, 50)
pitch.start(0)
yawing = GPIO.PWM(18, 50)
yawing.start(0)
roll = GPIO.PWM(24, 50)
roll.start(0)

# assign global min and max values
th_min = 1100
th_max = 2400
r_min = 1100
r_max = 1900
p_min = 1100
p_max = 1900
y_min = 1100
y_max = 1900
a_min = 980
a_max = 2300
throttle = 1100 #throttle
roll = 1520     #alleron
pitch = 1520    #elevator
yawing = 1520   #rudder


try:
    while 1:
        for dc in range(0, 1100,20):
            throttle.ChangeDutyCycle(dc)
			#yawing.ChangeDutyCycle(dc)
		    time.sleep(0.1) 
        #yawing = GPIO.PWM(18, 1520)		#system is armed
			 print ('system armed')
		throttle=1100
		while (throttle < requiredthrottlevalue) #based on required altitude time has to set	 
			throttle = throttle + 10
			if (throttle < th_min):
			 dc = 1100
			 throttle.ChangeDutyCycle(dc)
		    elif (th > th_max):
		     dc = 2400
			 throttle.ChangeDutyCycle(dc)
		    elif (throttle > th_min & throttle < th_max):
			  for dc in range(throttle ,2400,20): #corresponding throttle to required altitude
              throttle.ChangeDutyCycle(dc)
			  time.sleep(0.1)    				  #will be at defined at end of loop
		file=open("xyz.txt","r")
        contents=file.read()
        distance=contents[contents.find(":")+1:contents.find("\n")]
        file.seek(contents.find(":")+1)
        contents=file.read()
        angle=contents[contents.find(":")+1:]
        while(distance > 5 )
		    if ( pitch < p_min)
			    pitch = GPIO.PWM(13, 1100)
			elif( pitch > p_max)
			    pitch = GPIO.PWM(13,1520)
			elif (pitch > p_min & pitch < p_max):	
				pitch = GPIO.PWM(13,1520)			#movingforward             
				time.sleep(2)      					#resolution time
				file=open("xyz.txt","r")
                contents=file.read()
                distance=contents[contents.find(":")+1:contents.find("\n")]
				
			  #for dc in range(1100, 1900,10):
              #pitch.ChangeDutyCycle(dc)
		      #time.sleep(0.1)		           #its moving forward
		throttle = GPIO.PWM(12,1520)
        time.sleep(0.2)		                    #landing
		for dc in range(1520,-5 ,-20):
         throttle.ChangeDutyCycle(dc)
		 time.sleep(0.2)
        throttle.stop(0)
		pitch.stop(0)
		yawing.stop(0)
		roll.stop(0)
		
	
except KeyboardInterrupt:
    pass
pitch.stop(0)
GPIO.cleanup()
