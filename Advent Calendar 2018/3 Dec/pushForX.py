#By connecting the push button switch to 3.3V and P0, we can influence the display.
#Can you work out how to do with with button A or button B?

from microbit import *

while True:
    if pin0.read_digital():
        display.show("X")
    else:
        display.clear()