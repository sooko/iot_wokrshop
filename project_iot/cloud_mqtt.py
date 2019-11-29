from machine import Pin,Timer
from wifi import Wifi
import umqttsimple     
import machine
from umqttsimple import MQTTClient
from alldevice import led_blue,led_red

import ubinascii
import time
class Mqtt(object):

    wifi=Wifi()
    wifi.connect()
    client_id = ubinascii.hexlify(machine.unique_id())
    topic=b"ruang_tamu"
    def __init__(self, *args, **kwargs):
        super(Mqtt,self).__init__(*args, **kwargs)
        self.client = MQTTClient(self.client_id,"m16.cloudmqtt.com",port=10490 ,user='xemuautu', password='Yt6Le6V-YRfX')
        try:
            print("mqtt sedang berjalan dan menunggu message dengan topic= {} ".format(self.topic))
            self.client.connect()
            self.client.set_callback(self.sub_cb)
            self.client.subscribe(self.topic)
            while True:
                self.client.wait_msg()
        except:
            print("koneksi wifi atau server terputus")
            time.sleep(5)
            led_red.value(1)
            machine.reset()

    def sub_cb(self,topic,msg):
        print(topic,msg)
        if msg==b"led_on":
            led_blue.value(1)
        if msg==b"led_off":
            led_blue.value(0)
            
Mqtt()
