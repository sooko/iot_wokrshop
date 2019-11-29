FOR LINUX

install virtual environment
$ python3 -m pip install --upgrade --user pip setuptools 
$ python3 -m virtualenv ~/iot_workshop
$ source ~/iot_workshop/bin/activate


install esptool
$ pip install esptool

install adafruit-ampy
$ pip install adafruit-ampy


set permition
$ sudo usermode -a -G dialout <user>
$ sudo apt-get remove modemmanager
$ sudo reboot



FOR WINDOWS
install driver ch340
install esptool
$ pip install esptool
install adafruit-ampy
$ pip install adafruit-ampy


download firmware micropython for es8266
- masuk ke directory firmware
$  esptool.py --port /dev/ttyUSB0 erase_flash
$  esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20190529-v1.11.bin

