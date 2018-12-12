# Alarms if the light goes out.
# Wire up as the instructions on https://www.littlebird.com.au/learn/94/create-a-light-sensitive-alarm-with-micro-bit
# Which other sensors could you use to trigger the alarm?
# Could you you multiple sensors to trigger the alarm?

from microbit import *

while True:
#    pin0.write_digital(1)
    value = pin1.read_analog()
#    print(value)
    if value > 250:
        display.show('D')
        pin0.write_digital(0)
    else:
        display.show('L')
        pin0.write_digital(1)
    sleep(100)