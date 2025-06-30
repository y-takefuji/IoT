import pyfirmata
from time import sleep
b=pyfirmata.Arduino('COM4')
#b=pyfirmata.Arduino('/dev/cu.XXXXX')
b.digital[2].write(1)
sleep(10)
