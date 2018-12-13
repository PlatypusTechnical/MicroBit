# Display hello world on the ssd1306 OLED (128x64) screen
# Requires the SSD1306 library from https://github.com/fizban99/microbit_ssd1306
# Wiring as per https://www.littlebird.com.au/learn/77/0-96-oled-screen-with-micro-bit

from microbit import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text

def displayLevel(level):
#    print(level)
    pixels = ['0'] * 20
    for i in range(0,5):
        pixels.insert(level*5 + i, '5')
#    print(pixels)
    
    # Creat a microbit image and display
    pixels.insert(20,':')
    pixels.insert(15,':')
    pixels.insert(10,':')
    pixels.insert(5,':')
    tempDot = Image("".join(pixels))
    display.show(tempDot)
#    display.show(str(potValue))

initialize()
clear_oled()
time = "Daytime"
rainThreshold = 600
rain = "Raining"
action = "Play outside"
while True:
    LDRvalue = pin1.read_analog()
    if LDRvalue < 250:
        time = "Day time  "
    else:
        time = "Night time"
    
    potValue = pin0.read_analog()
    setting = int(potValue / 250)
    displayLevel(setting)
    rainLevel = pin2.read_analog()
    if rainLevel > potValue:
        rain = "Dry    "
    else:
        rain = "Raining"
    
    if (time == "Night time") or (rain == "Raining"):
        action = "Play inside "
    else:
        action = "Play outside"
    
    add_text(0,0, time)
    add_text(0,1, rain)
    add_text(0,3, action)
    sleep(100)