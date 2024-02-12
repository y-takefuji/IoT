import pyfirmata
from time import sleep
b=pyfirmata.Arduino('COM3')
a5=b.get_pin('a:5:i')
i = pyfirmata.util.Iterator(b)
i.start()
b.analog[5].enable_reporting()
while 1:
 if a5.read() == None:
  pass
 else:
  print(a5.read())
  sleep(1)
