# This is similar to the 1 Dec flashing LED code,
# expect that we can program a light show by choosing which order and how quickly to turn LED on and off.
# The display is turned off to make pins 3, 4, 6, 7, 9 available.
# Pin5 is tied to button_a, so we don't use it.
# Can you modify this code to make your own light show?

from microbit import *

display.off()

while True:
    for i in range(0,2):
        pin0.write_digital(1)
        sleep(50)
        pin1.write_digital(1)
        sleep(50)
        pin2.write_digital(1)
        sleep(50)
        pin3.write_digital(1)
        sleep(50)
        pin4.write_digital(1)
        sleep(50)
        pin6.write_digital(1)
        sleep(50)
        pin7.write_digital(1)
        sleep(50)
        pin8.write_digital(1)
        sleep(50)
        pin9.write_digital(1)
        sleep(50)
        
        pin0.write_digital(0)
        sleep(50)
        pin1.write_digital(0)
        sleep(50)
        pin2.write_digital(0)
        sleep(50)
        pin3.write_digital(0)
        sleep(50)
        pin4.write_digital(0)
        sleep(50)
        pin6.write_digital(0)
        sleep(50)
        pin7.write_digital(0)
        sleep(50)
        pin8.write_digital(0)
        sleep(50)
        pin9.write_digital(0)
        sleep(50)
    
    #Red/blue
    for i in range(0,10):
        pin2.write_digital(1)
        sleep(200)
        pin2.write_digital(0)
        pin6.write_digital(1)
        sleep(200)
        pin6.write_digital(0)
      
    #Red,yello,green  
    pin2.write_digital(1)
    sleep(200)
    pin1.write_digital(1)
    pin3.write_digital(1)
    sleep(200)
    pin0.write_digital(1)
    pin4.write_digital(1)
    sleep(50)
    for i in range(0,20):
        pin0.write_digital(1)
        pin1.write_digital(1)
        pin2.write_digital(1)
        pin3.write_digital(1)
        pin4.write_digital(1)
        sleep(50)
        pin0.write_digital(0)
        pin1.write_digital(0)
        pin2.write_digital(0)
        pin3.write_digital(0)
        pin4.write_digital(0)
        sleep(50)
    
    pin0.write_digital(1)
    pin1.write_digital(1)
    pin2.write_digital(1)
    pin3.write_digital(1)
    pin4.write_digital(1)
    sleep(50)
    pin0.write_digital(0)
    pin4.write_digital(0)
    sleep(200)
    pin1.write_digital(0)
    pin3.write_digital(0)
    sleep(200)
    pin2.write_digital(0)
    sleep(50)
    
    #Blue/white
    for i in range(0,5):
        pin6.write_digital(1)
        sleep(50)
        pin7.write_digital(1)
        sleep(50)
        pin8.write_digital(1)
        sleep(50)
        pin9.write_digital(1)
        sleep(250)
        
        pin9.write_digital(0)
        sleep(250)
        pin8.write_digital(0)
        sleep(250)
        pin7.write_digital(0)
        sleep(250)
        pin6.write_digital(0)
        sleep(250)
        
    #All
    for i in range(0,50):
        pin0.write_digital(1)
        pin1.write_digital(1)
        pin2.write_digital(1)
        pin3.write_digital(1)
        pin4.write_digital(1)
        pin6.write_digital(1)
        pin7.write_digital(1)
        pin8.write_digital(1)
        pin9.write_digital(1)
        sleep(25)
        
        pin0.write_digital(0)
        pin1.write_digital(0)
        pin2.write_digital(0)
        pin3.write_digital(0)
        pin4.write_digital(0)
        pin6.write_digital(0)
        pin7.write_digital(0)
        pin8.write_digital(0)
        pin9.write_digital(0)
        sleep(25)
    