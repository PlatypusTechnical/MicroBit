# Cycles through the primary and secondary colours of light, as well as white.
# Need a RGB LED to be wired up.  Instructions are Step 7 on https://www.littlebird.com.au/learn/63/make-an-rgb-led-blink-with-micro-bit
# Video of the code running is available at https://www.youtube.com/watch?v=mNEN9i9zddM

from microbit import *

while True:
    #Red
    pin1.write_digital(0)
    pin2.write_digital(0)
    sleep(500)
    #Yellow
    pin1.write_digital(1)
    sleep(500)
    #Green
    pin0.write_digital(0)
    sleep(500)
    #Cyan
    pin2.write_digital(1)
    sleep(500)
    #Blue
    pin1.write_digital(0)
    sleep(500)
    #Magenta
    pin0.write_digital(1)
    sleep(500)
    #White
    pin1.write_digital(1)
    sleep(500)