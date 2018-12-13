# Alarms if a magent is detected by the reed switch.
# Using the instructions in https://www.littlebird.com.au/learn/83/reed-switch-with-micro-bit,
#   can you work our how to wire in the buzzer without the LED?
# A reed switch needs a reversed magnetic field to open it again.  Can you create a field that switches directions?

from microbit import *

while True:
    value = pin1.read_digital()
    if value:
        display.clear()
        pin0.write_digital(1)
    else:
        display.show('M')
        pin0.write_digital(0)
    sleep(100)