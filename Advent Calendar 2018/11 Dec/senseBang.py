# Uses the sound sensor to control the micro:bit display.
# Wire up as the instructions on https://www.littlebird.com.au/learn/80/sound-sensor-with-micro-bit
# How loud do you have to clap/bang to make the screen change?
# How do you change the sound threshold?

from microbit import *

while True:
    value = pin1.read_analog()
    print(value)
    if value > 30:
        display.show('L')
    else:
        display.show('S')
    sleep(100)