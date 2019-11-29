import paho.mqtt.publish as publish   #import library mqtt
# publish.single("ruang_tamu", "led_on", hostname="m16.cloudmqtt.com",port=10490,auth={'username':"xemuautu", 'password':"Yt6Le6V-YRfX"})
publish.single("ruang_tamu", "led_off", hostname="192.168.1.7")
