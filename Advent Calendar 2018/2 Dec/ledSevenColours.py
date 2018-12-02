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