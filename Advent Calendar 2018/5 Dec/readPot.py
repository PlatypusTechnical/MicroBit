# Control the letter on the micro:bit display using the knob
# Use the wiring shown in Step 5 of https://www.littlebird.com.au/learn/81/control-led-brightness-using-a-potentiometer

from microbit import *

value = 0
while True:
    value = pin0.read_analog()
    number = int(value/1023 * 25)
    letter = chr(number+65)
#    print(letter)
    display.show(letter)
    sleep(100)