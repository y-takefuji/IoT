import pyfirmata
from time import sleep
b=pyfirmata.Arduino('COM4')
b.digital[2].write(1)
