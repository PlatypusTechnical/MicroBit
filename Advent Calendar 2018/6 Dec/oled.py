# Display hello world on the ssd1306 OLED (128x64) screen
# Requires the SSD1306 library from https://github.com/fizban99/microbit_ssd1306
# Wiring as per https://www.littlebird.com.au/learn/77/0-96-oled-screen-with-micro-bit

from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text

initialize()
clear_oled()
add_text(0,2, "Hello, World!")
