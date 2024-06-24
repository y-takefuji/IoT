import pyfirmata
from time import sleep
b=pyfirmata.Arduino('COM4')
#i=pyfirmata.util.Iterator(b)
b.digital[2].write(0)
