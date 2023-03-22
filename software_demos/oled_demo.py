from machine import Pin, I2C
import ssd1306
import time


# using default address 0x3C
i2c = I2C(0, sda=Pin(4), scl=Pin(5))
time.sleep(1)
display = ssd1306.SSD1306_I2C(128, 32, i2c)
time.sleep(1)
# rotaryA = Pin(16, Pin.IN, Pin.PULL_DOWN)
# rotaryB = Pin(17, Pin.IN, Pin.PULL_DOWN)display.fill(0)
display.fill_rect(0, 0, 32, 32, 1)
display.fill_rect(2, 2, 28, 28, 0)
display.vline(9, 8, 22, 1)
display.vline(16, 2, 22, 1)
display.vline(23, 8, 22, 1)
display.fill_rect(26, 24, 2, 4, 1)
display.text('MicroPython', 40, 0, 1)
display.text('SSD1306', 40, 12, 1)
display.text('OLED 128x64', 40, 24, 1)
display.show()