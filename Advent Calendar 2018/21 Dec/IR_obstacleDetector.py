# Use the wiring from: https://www.littlebird.com.au/learn/92/preview?key=hpwych9eYWYmFmbu
# This python code will turn the LED on when an obstacle gets 'too close' to the IR module.
# How close is too close is determined by the value of the threshold variable.

from microbit import *

threshold = 50
value = 0

while True:
    value = pin0.read_analog()
    if value < 50:
        pin1.write_digital(1)
    else:
        pin1.write_digital(0)
    sleep(100)