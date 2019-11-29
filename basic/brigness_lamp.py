from alldevice import *
import time
brigness_led=PWM(led_blue)

while True:
    print(ldr.read())
    brigness_led.freq(1024)
    brigness_led.duty(1024-ldr.read())
    time.sleep(.1)



