# Instalasi

<!-- install tools and burn micropython firmware to esp8266 board -->

## for windows
- python-3.7.2-amd64.exe


- install putty-0.73-installer.msi


- install VSCodeUserSetup-x64-1.40.0.exe


- install driver CH34x_Install_Windows_v3_4.EXE

## for linux
- install gtkterm or screen for serial monitor

```bash
sudo apt-get install gtkterm
```
```bash
sudo apt-get install screen
```



## install tools for micropython with pip

- install esptool
```bash
pip install esptool
```
- install adafruit-ampy
```bash
pip install adafruit-ampy
```

## burn firmware micropython to esp8266 

```bash
esptool.py --port /dev/ttyUSB0 erase_flash
```
- cd "folder firmware"
```bash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20190529-v1.11.bin
```



