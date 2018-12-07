# Take a raw reading from a thermistor module and uses the value to place a pixel on the display
# As temperature changes the dot will move around the display

from microbit import *
value = 0
while True:
    value = pin1.read_analog()
    #There are 25 pixels on the microbit display
    #transform values between 800 and 1000 to be a number between 0 and 24
    value = value - 800
    value = int(value / 12.5)
    
    #Make a list of zeros to represent the pixels, and insert a 5 where the dot should be
    pixels = ['0'] * 25
    pixels[value] = '5'
    print(pixels)
    
    # Creat a microbit image and display
    pixels.insert(20,':')
    pixels.insert(15,':')
    pixels.insert(10,':')
    pixels.insert(5,':')
    tempDot = Image("".join(pixels))
    display.show(tempDot)
    
    sleep(500)