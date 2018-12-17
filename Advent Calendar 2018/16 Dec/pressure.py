from microbit import *
import time

import bmp280

b = bmp280.BMP280(i2c)

while True:
    time.sleep_ms(500)
    b.get()