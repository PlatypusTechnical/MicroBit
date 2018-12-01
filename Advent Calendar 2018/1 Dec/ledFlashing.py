from microbit import *

while True:
    pin0.write_digital(1)
    display.scroll("Red")
    pin1.write_digital(1)
    pin0.write_digital(0)
    display.scroll("Green")