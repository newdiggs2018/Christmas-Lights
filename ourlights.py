#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [12, 16, 20, 21, 6, 13, 19, 26]

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = .9

# main loop

try:
  GPIO.output(12, GPIO.LOW)
  print "ONE"
  time.sleep(SleepTimeL); 
  GPIO.output(16, GPIO.LOW)
  print "TWO"
  time.sleep(SleepTimeL);  
  GPIO.output(20, GPIO.LOW)
  print "THREE"
  time.sleep(SleepTimeL);
  GPIO.output(21, GPIO.LOW)
  print "FOUR"
  time.sleep(SleepTimeL);
  GPIO.output(6, GPIO.LOW)
  print "FIVE"
  time.sleep(SleepTimeL);
  GPIO.output(13, GPIO.LOW)
  print "SIX"
  time.sleep(SleepTimeL);
  GPIO.output(19, GPIO.LOW)
  print "SEVEN"
  time.sleep(SleepTimeL);
  GPIO.output(26, GPIO.LOW)
  print "EIGHT"
  time.sleep(SleepTimeL);
  #clean up pins and end
  GPIO.cleanup()
  print "Good bye!"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit & Clean up used pins"
  # Reset GPIO settings
  GPIO.cleanup()


# find more information on this script at
# http://youtu.be/oaf_zQcrg7g
