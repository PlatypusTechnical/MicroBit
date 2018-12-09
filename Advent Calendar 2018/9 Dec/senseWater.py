# Uses the rain sensor to decide if it is wet or dry.
# Wire up as the instructions on https://www.littlebird.com.au/learn/82/raindrop-sensor-with-micro-bit
# How many drops does it take for it to be wet?
# How do you change the threshold for wet/dry?

from microbit import *

while True:
    value = pin1.read_analog()
#    print(value)
    if value > 600:
        display.show('D')
    else:
        display.show('W')
    sleep(100)