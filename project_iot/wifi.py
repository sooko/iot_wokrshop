import network
from machine import Pin
from alldevice import *

print("mengubungkan ......")
class Wifi(object):
    ssid = "HANS"
    password = "sooko1989"
    station = network.WLAN(network.STA_IF)
    state=""
    def __init__(self, *args, **kwargs):
        super(Wifi,self).__init__(*args, **kwargs)
    def connect(self):
        if self.station.isconnected() == True:
            self.state="telah terhubung"
            return
        self.station.active(True)
        self.station.disconnect()
        self.station.connect(self.ssid, self.password)
        while self.station.isconnected() == False:
            self.state="mencoba terhubung ....."
            led_red.value(1)
            led_green.value(0)
            pass
        print("sukses terhubung")
        self.state="terhubung"
        print(self.station.ifconfig())
        led_red.value(0)
        