from alldevice import led_red,led_blue,led_green
import time

while True:
    led_red.value(0)
    led_green.value(0)
    led_blue.value(0)
    time.sleep(1)
    led_red.value(1)
    led_green.value(1)
    led_blue.value(1)
    time.sleep(1)
    














# led_red.value(not led_red.value())
# led_green.value(not led_green.value())
# led_blue.value(not led_blue.value())