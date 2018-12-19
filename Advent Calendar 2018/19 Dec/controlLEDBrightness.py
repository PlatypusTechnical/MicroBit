# This code uses a rotary encoder to control the brightness of some LEDs.
# THis coundl be used to adjust the brighness of our 18 Dec Christmas lights
# Can you work our how to combine the 18 Dec code with this code to control the brighness of your light show?

# Wiring for encoder:
#   - GND is connected to GND
#   - + is connected to 3.3V
#   - CLK is connected to pin11 (encoder1)
#   - DT is connected to pin12 (encoder2)
#   - SW is not needed

#Wiring for LEDs:
#   - LEDs (with resistors) are wired to pins 0 to 4.
#       - See Step 14 of: https://www.littlebird.com.au/learn/89/using-leds-with-micro-bit

from microbit import *

display.off()
encoder1_value = 0
encoder2_value = 0
encoder1_previous = 0
encoder2_previous = 0

count = 0

while True:
    encoder1_value = pin11.read_digital()
    if encoder1_value != encoder1_previous:
        encoder2_value = pin12.read_digital()
        if encoder2_value != encoder2_previous:
            count = count +5
        else:
            count = count -5
    
    if count > 1023:
        count = 1023
    if count < 0:
        count = 0
    
    encoder1_previous = encoder1_value
    encoder2_previous = encoder2_value
    pin0.write_analog(count)
    pin1.write_analog(count)
    pin2.write_analog(count)
    pin3.write_analog(count)
    pin4.write_analog(count)