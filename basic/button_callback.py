from alldevice import button,led_blue
from machine import Pin

class Btn(object):
    btn=button
    def __init__(self,*args,**kwargs):
        super(Btn,self).__init__(*args,**kwargs)
        self.btn.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self.callback)
            

    def callback(self,btn):
        led_blue.value(btn.value())
        self.got_value(btn.value())

    def got_value(self,data):
        pass


















# Btn()