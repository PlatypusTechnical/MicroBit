# The LED turns on if a magent is detected by the hall-effect sensor.
# Using the wiring instructions from https://www.littlebird.com.au/learn/90/hall-effect-sensor-with-micro-bit
# This code is very similar to what was done with the reed switch and the other binary sensors/switches.

from microbit import *

while True:
    pin1.write_digital(0)
    value = pin0.read_digital()
    if value:
        display.clear()
        pin1.write_digital(0)
    else:
        display.show('M')
        pin1.write_digital(1)
    sleep(100)