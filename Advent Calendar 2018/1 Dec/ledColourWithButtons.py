from microbit import *

while True:
    sleep(20)
    if button_a.was_pressed():
        pin1.write_digital(0)
        pin0.write_digital(1)
        display.scroll("Red")
    if button_b.was_pressed():
        pin1.write_digital(1)
        pin0.write_digital(0)
        display.scroll("Green")
    pin0.write_digital(0)
    pin1.write_digital(0)