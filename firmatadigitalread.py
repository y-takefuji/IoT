import pyfirmata
from time import sleep
b=pyfirmata.Arduino('COM3')
i=pyfirmata.util.Iterator(b)
i.start()
pin2=b.get_pin('d:2:i')
while 1:
 print(pin2.read())
 sleep(1.5)
