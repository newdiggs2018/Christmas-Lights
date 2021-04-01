#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [12, 16, 20, 21, 6, 13, 19, 26]

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 0.2
# Pin is 0 thru 7: state is 0 or 1, 1 meaning on.
def setrelay(pin,state):
	global pinList
	gpioNumber = pinList[pin]
	if state:
		GPIO.output(gpioNumber, GPIO.LOW)
	else:
		GPIO.output(gpioNumber, GPIO.HIGH)
		
def bottomFloor(state):
	setrelay(0,state)
	setrelay(1,state)
	setrelay(2,state)
	setrelay(3,state)	
	
def topFloor(state):
	setrelay(4,state)
	setrelay(5,state)
	setrelay(6,state)
	setrelay(7,state)
	
def allLights(state):
	setrelay(0,state)
	setrelay(1,state)
	setrelay(2,state)
	setrelay(3,state)	
	setrelay(4,state)
	setrelay(5,state)
	setrelay(6,state)
	setrelay(7,state)			

def leftHalf(state):
	setrelay(0,state)
	setrelay(1,state)
	setrelay(4,state)
	setrelay(5,state)
	
def rightHalf(state):
	setrelay(2,state)
	setrelay(3,state)
	setrelay(6,state)
	setrelay(7,state)	
	
def outsideHalf(state):
	setrelay(0,state)
	setrelay(3,state)
	setrelay(4,state)
	setrelay(7,state)	

def insideHalf(state):
	setrelay(1,state)
	setrelay(2,state)
	setrelay(5,state)
	setrelay(6,state)

def evenHalf(state):
	setrelay(0,state)
	setrelay(2,state)
	setrelay(4,state)
	setrelay(6,state)

def oddHalf(state):
	setrelay(1,state)
	setrelay(3,state)
	setrelay(5,state)
	setrelay(7,state)


# Here begins sequences
def sequenceVertical():
	for index in xrange(2):
		bottomFloor(1)
		topFloor(0)	
		time.sleep(0.2)
		
		bottomFloor(0)
		topFloor(1)	
		time.sleep(0.2)
	
def sequenceHorizontal():
	for index in xrange(2):
		rightHalf(1)
		leftHalf(0)	
		time.sleep(0.2)
		
		rightHalf(0)
		leftHalf(1)	
		time.sleep(0.2)	
	
def sequenceOddEven():
	for index in xrange(2):
		oddHalf(1)
		evenHalf(0)	
		time.sleep(0.4)
		
		oddHalf(0)
		evenHalf(1)	
		time.sleep(0.4)	

		
def sequenceClockwiseFill():
	allLights(0)
	time.sleep(0.2)
	for index in xrange(2):
		setrelay(6,1)
		time.sleep(0.2)
		setrelay(7,1)
		time.sleep(0.2)
		setrelay(3,1)
		time.sleep(0.2)
		setrelay(2,1)
		time.sleep(0.2)
		setrelay(1,1)
		time.sleep(0.2)
		setrelay(0,1)
		time.sleep(0.2)
		setrelay(4,1)
		time.sleep(0.2)
		setrelay(5,1)
		time.sleep(0.2)

# untested yet		
def sequenceStitchRightUp():
	allLights(0)
	time.sleep(0.2)
	lightsSRU = [0, 5, 2, 7, 3, 6, 1, 4]
	for index in xrange(8):
		setrelay(lightsSRU[index],1)
		time.sleep(0.3)
		setrelay(lightsSRU[index],0)
		time.sleep(0.1)
		
# untested yet		
def sequenceStitchLeftUp():
	allLights(0)
	time.sleep(0.2)
	lightsSLU = [3, 6, 1, 4, 0, 5, 2, 7]
	for index in xrange(8):
		setrelay(lightsSLU[index],1)
		time.sleep(0.3)
		setrelay(lightsSLU[index],0)
		time.sleep(0.1)		
				
		
def sequenceCounterClockwiseFill():
	allLights(0)
	time.sleep(0.4)
	for index in xrange(1):
		setrelay(5,1)
		time.sleep(0.4)
		setrelay(4,1)
		time.sleep(0.4)
		setrelay(0,1)
		time.sleep(0.4)
		setrelay(1,1)
		time.sleep(0.4)
		setrelay(2,1)
		time.sleep(0.4)
		setrelay(3,1)
		time.sleep(0.4)
		setrelay(7,1)
		time.sleep(0.4)
		setrelay(6,1)
		time.sleep(0.4)		
		

def sequenceClockwiseSnake():
	snakeLength = 3
	allLights(0)
	time.sleep(0.3)
	lights = [6,7,3,2,1,0,4,5]
	for index in xrange(16):
		setrelay(lights[(index+0)%8],1)
		setrelay(lights[(index+8-snakeLength)%8],0)
		time.sleep(0.2)	
		
def sequenceCounterClockwiseSnake():
	snakeLength = 3
	allLights(0)
	time.sleep(0.3)
	lights = [5,4,0,1,2,3,7,6]
	for index in xrange(16):
		setrelay(lights[(index+0)%8],1)
		setrelay(lights[(index+8-snakeLength)%8],0)
		time.sleep(0.2)			
		
			
		
				
		
# main loop

try:
 	sequences = [sequenceClockwiseSnake, sequenceVertical, sequenceHorizontal, sequenceOddEven,
                 sequenceCounterClockwiseFill, sequenceClockwiseFill, sequenceCounterClockwiseSnake,
                 sequenceStitchRightUp, sequenceStitchLeftUp]
#	sequences = [sequenceStitchRightUp, sequenceStitchLeftUp]
#	for index in xrange(20):
	while(True):
		seq = random.randint(0, len(sequences)-1)
		sequences[seq]()
		
	
	GPIO.cleanup()
# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()


