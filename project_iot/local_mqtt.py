from machine import Pin,Timer
from wifi import Wifi
import umqttsimple     
import machine
from umqttsimple import MQTTClient
from alldevice import led_blue,led_green
import ubinascii
import time
class Mqtt(object):
    wifi=Wifi()
    wifi.connect()
    client_id = ubinascii.hexlify(machine.unique_id())
    server="192.168.1.7"
    topic=b"ruang_tamu"
    
    def __init__(self, *args, **kwargs):
        super(Mqtt,self).__init__(*args, **kwargs)
        self.client = MQTTClient(self.client_id,self.server)
        
        try:
            led_green.value(1)
            print("mqtt sedang berjalan dan menunggu message dengan topic= {} ".format(self.topic))
            self.client.connect()
            self.client.set_callback(self.sub_cb)
            self.client.subscribe(self.topic)
            while True:
                self.client.wait_msg()
        except:
            print("koneksi wifi atau server terputus")
            led_green.value(0)
            time.sleep(5)
            machine.reset()
            
    def sub_cb(self,topic,msg):
        print("topic   ={}".format(topic.decode()))
        print("message = {}".format(msg.decode()))
        
        if msg==b"led_on":
            led_blue.value(1)
        if msg==b"led_off":
            led_blue.value(0)

Mqtt()
