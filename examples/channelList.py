# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685
from random import randint
from sys import exit


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
# servo_min = 150  # Min pulse length out of 4096
# servo_max = 600  # Max pulse length out of 4096
df1=1000###doit etre un entier compris entre 0 et 4095 
df2=3000
freq=100 #Hz
# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= freq       # freq en HzHz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 2000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(freq)
for i in range(15):  #mise a zero de securite
    pwm.set_pwm(i, 0, 0)

# chanList=[1,2,3,4]
chanList=[i for i in range(1,17)]
dfList=[df1 for i in chanList]
# print(dfList)
# print(chanList)
# exit()
# dfList=[]
# for i in range(16):
#     dfList.append(randint(0,4090))
# dfList.sort()
# print([6.6*stuff/4095 for stuff in dfList])
# exit()
for i in chanList:
    pwm.set_pwm(i-1, 0, dfList[chanList.index(i)])

# pwm.set_pwm(0, 0, df1)
# pwm.set_pwm(1, 0, df2)
print('ca tourne')
time.sleep(500)
# for i in range(10):

for i in chanList:
    pwm.set_pwm(i-1, 0, 0)

# print('Moving servo on channel 0, press Ctrl-C to quit...')
# while True:
#     # Move servo on channel O between extremes.
#     pwm.set_pwm(0, 0, df)
#     # time.sleep(1)
#     # pwm.set_pwm(0, 0, servo_max)
#     # time.sleep(1)
