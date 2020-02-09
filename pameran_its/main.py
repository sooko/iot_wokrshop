from kivy.lang import Builder
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
Config.set('graphics', 'height', 770)
Config.set('graphics', 'width', 370)
Builder.load_file("ml.kv")
Builder.load_file("saklar.kv")
Builder.load_file("popchoise.kv")
Builder.load_file("monitor.kv")
from kivy.uix.slider import Slider
from plyer import uniqueid
Builder.load_file("pwm.kv")

import ast
import paho.mqtt.publish as publish
from css import Btn,BtnImg
from kivy.storage.jsonstore import JsonStore
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.properties import StringProperty,NumericProperty,ListProperty,DictProperty
import paho.mqtt.client as paho
import threading
import random
import sys
from kivy.core.window import Window
from kivy.clock import Clock
import time
from jnius import autoclass
from kivy.utils import platform

class PopChoise(FloatLayout):
    def __init__(self, **kwargs):
        self.register_event_type("on_pilih_widget")
        super(PopChoise,self).__init__(**kwargs)
    def press(self,instance):
        self.dispatch("on_pilih_widget",instance)
    def on_pilih_widget(self,instance):
        pass
class Sld(Slider):
    triger=NumericProperty(0)
    def __init__(self, **kwargs):
        super(Sld,self).__init__(**kwargs)
    def on_touch_up(self, touch):
        # if self.collide_point(*touch.pos):
            # print("ok")
        self.triger+=1
        return super(Sld,self).on_touch_up(touch)
    def on_touch_down(self, touch):
        # if self.collide_point(*touch.pos):
            # print("ok")
        self.triger+=1
        return super(Sld,self).on_touch_down(touch)
class Saklar(FloatLayout):
    device_name=StringProperty("Saklar")
    topic=StringProperty("saklar")
    message1=StringProperty("on")
    message2=StringProperty("off")
    tittle=StringProperty("saklar")
    status=StringProperty("off")
    state=StringProperty("normal")
    status_color=ListProperty([1,0,0,1])
    value=StringProperty("")
    def __init__(self, **kwargs):
        super(Saklar,self).__init__(**kwargs)
    def edit(self,instance):
        self.ids["sm"].current="edit"
class Pwm(FloatLayout):
    device_name=StringProperty("Slider")
    topic=StringProperty("slider")
    message1=StringProperty("0")
    message2=StringProperty("100")
    tittle=StringProperty("slider")
    status=StringProperty("0")
    state=StringProperty("normal")
    status_color=ListProperty([.5,1,0,1])
    value=StringProperty("")
    def __init__(self, **kwargs):
        super(Pwm,self).__init__(**kwargs)
    def edit(self,instance):
        self.ids["sm"].current="edit"
class Monitor(FloatLayout):
    device_name=StringProperty("Monitor")
    topic=StringProperty("monitor")
    message1=StringProperty("0")
    message2=StringProperty("100")
    tittle=StringProperty("monitor")
    status=StringProperty("0")
    state=StringProperty("normal")
    status_color=ListProperty([.5,1,0,1])
    # label_connect=Str
    value=StringProperty("")
    def __init__(self, **kwargs):
        super(Monitor,self).__init__(**kwargs)
    def edit(self,instance):
        self.ids["sm"].current="edit"
class Ml(FloatLayout):
    dict_children=DictProperty({})
    paho=paho
    server=StringProperty("192.168.xxx")
    mqtt_state=StringProperty("not connect")
    client=None
    read_thread=None
    storage=JsonStore("data_server.json")
    storage_widget=JsonStore("widget.json")
    storage_mqtt_state=JsonStore("mqtt_state.json")
    
    child=ListProperty([])
    tutup=False
    rc=1000
    def __init__(self, **kwargs):
        super(Ml,self).__init__(**kwargs)
        self.load()
        self.ids["pc"].on_pilih_widget=self.on_pilih_widget
        self.client = self.paho.Client(uniqueid.id)#(str(random.randint(1,2000)))
        self.client.on_connect=self.connecting
        self.client.on_message = self.on_message
        Window.bind(on_keyboard=self.back)
        if self.mqtt_state=="connected":
            self.connect()
        
    def load(self):
        try:
            li=[i for i in self.storage_widget]
            li.reverse()
            for i in li:
                if self.storage_widget.get(i)["score"][0]=="saklar":
                    print(i)
                    self.ids["root_widget"].add_widget(Saklar(
                        device_name =self.storage_widget.get(i)["score"][1],
                        topic       =self.storage_widget.get(i)["score"][2],
                        status      =self.storage_widget.get(i)["score"][3],
                        message1    =self.storage_widget.get(i)["score"][4],
                        message2    =self.storage_widget.get(i)["score"][5],
                        state       =self.storage_widget.get(i)["score"][6],
                        status_color=self.storage_widget.get(i)["score"][7]
                        
                        ))
                if self.storage_widget.get(i)["score"][0]=="slider":
                    print(i)
                    self.ids["root_widget"].add_widget(Pwm(
                        device_name =self.storage_widget.get(i)["score"][1],
                        topic       =self.storage_widget.get(i)["score"][2],
                        status      =self.storage_widget.get(i)["score"][3],
                        message1    =self.storage_widget.get(i)["score"][4],
                        message2    =self.storage_widget.get(i)["score"][5],
                        state       =self.storage_widget.get(i)["score"][6],
                        status_color=self.storage_widget.get(i)["score"][7]

                        ))
                if self.storage_widget.get(i)["score"][0]=="monitor":
                    print(i)
                    self.ids["root_widget"].add_widget(Monitor(
                        device_name =self.storage_widget.get(i)["score"][1],
                        topic       =self.storage_widget.get(i)["score"][2],
                        status      =self.storage_widget.get(i)["score"][3],
                        message1    =self.storage_widget.get(i)["score"][4],
                        message2    =self.storage_widget.get(i)["score"][5],
                        state       =self.storage_widget.get(i)["score"][6],
                        status_color=self.storage_widget.get(i)["score"][7]
                        ))
            self.server=self.storage.get("han")["score"]
            self.mqtt_state=self.storage_mqtt_state.get("state")["score"]
        except:
            pass
    def start_connect(self,data,state):
        if state==False:
            self.server=data
            self.save(self.server)
            if self.client:
                try:
                    print("connecting...")

                    self.connect()
                except:
                    pass
    def connect(self):
        print("connect")
        if platform=="android":
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            PythonActivity.toastError("connecting...")
        try:
            if platform=="android":
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                PythonActivity.toastError("connected")
            self.mqtt_state="connected"
            self.storage_mqtt_state.put("state",score=self.mqtt_state)
            self.client.connect(self.server,keepalive=5)
            self.client.loop_start()
        except:
            if platform=="android":
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                PythonActivity.toastError("failed to connect to server")
            self.mqtt_state="not connect"
            self.storage_mqtt_state.put("state",score=self.mqtt_state)
    def connecting(self,client, userdata, flags, rc):
        self.rc=rc
        if self.client:
            self.client.subscribe("#")
    def disconnecting(self,client, userdata, rc, properties):
        print(rc)
    def on_message(self, client, userdata, message):
        self.mqtt_masuk = str(message.payload.decode("utf-8"))
        print(self.mqtt_masuk)
        tpc=message.topic
        for i in self.ids["root_widget"].children:
            if i.topic==tpc:
                i.status=self.mqtt_masuk

    def save(self,server):
        self.storage.put("han",score=server)
    def on_pilih_widget(self,data):
        if data=="saklar":
            self.ids["root_widget"].add_widget(Saklar())
        if data=="slider":
            self.ids["root_widget"].add_widget(Pwm())
        if data=="monitor":
            self.ids["root_widget"].add_widget(Monitor())
        self.ids["pc"].posisi=2
    def back(self,window,key,*largs):
        if key == 27:
            self.save_widget()
    def save_widget(self):
        self.storage_widget.clear()
        for i in self.ids["root_widget"].children:
            self.storage_widget.put(str(i),score=[i.tittle,i.device_name,i.topic,i.status,i.message1,i.message2,i.state,i.status_color])
    # def change(self):
    #     # print("cokkk")
    #     for i in self.ids["root_widget"].children:
    #         i.topic=i.topic
class MqttGui(App):
    ml=Ml()
    def build(self):
        return self.ml
    def publish(self,a,b):
        self.ml.client.publish(a,b)
    def on_pause(self):
        self.ml.save_widget()
        return True
    # def change(self):
    #     self.ml.change()
    
  
if __name__=="__main__":
    MqttGui().run()