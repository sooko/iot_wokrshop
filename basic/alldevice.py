# all devices that we will use in all projects

from machine import Pin,PWM,ADC 
led_red=Pin(4,Pin.OUT)
led_green=Pin(5,Pin.OUT)
led_blue=Pin(15,Pin.OUT)
ldr=ADC(0)
button=Pin(0, Pin.IN) 

print("alldevice ready")
