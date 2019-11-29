# mengetahui nilai adc dari sensor LDR


from alldevice import *
import time
while True:
    print(ldr.read())
    time.sleep(.1)

