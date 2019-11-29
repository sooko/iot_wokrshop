from alldevice import button,led_blue
import time

while True:
    print(button.value())
    led_blue.value(button.value())
    time.sleep(.5)
    