# Uses the gas sensor to decide if there are flammable gases around.
# Wire up using steps 1 to 6 of the Little Bird instructions on https://www.littlebird.com.au/learn/86/smoke-sensor-with-micro-bit
# I used a candle to test it.  Be careful!

from microbit import *

while True:
    value = pin1.read_analog()
    print(value)
    if value < 750:
        display.show(Image.HEART)
    else:
        display.show(Image.SKULL)
    sleep(100)