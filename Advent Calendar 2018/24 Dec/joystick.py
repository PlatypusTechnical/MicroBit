# This code uses an analogue joystick module to control a dot on the micro:bit display.
# Use the module and wiring from here: https://www.littlebird.com.au/learn/96/joystick-module-with-micro-bit
# What else could you use this joystick to control?
# Can you modify the wiring and code to do that?

from microbit import *

xVal = 0
yVal = 0
xCoord = 2
yCoord = 2

while True:
    xVal = pin1.read_analog()
    yVal = pin0.read_analog()
    
    xCoord = int(xVal * 4 /750)
    yCoord = int(yVal * 4 /750)
    
    row = ['0'] * 5
    row[xCoord] = '5'
    beforePixels = ['0'] * 5 * yCoord
    afterPixels = ['0'] *5 * (4-yCoord)
    pixels = beforePixels + row + afterPixels
    pixels.insert(20,':')
    pixels.insert(15,':')
    pixels.insert(10,':')
    pixels.insert(5,':')
    image = Image("".join(pixels))
    display.show(image)
    
    sleep(100)