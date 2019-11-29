from alldevice import *
import time

list_led=[led_red,led_green,led_blue]

while True:
    for i in list_led:
        i.value(1)
        time.sleep(.2)
        i.value(0)


